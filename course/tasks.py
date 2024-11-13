from django.core.mail import send_mail
from users.models import User
from celery import shared_task
from course.models import Course, Subscription
from config.settings import EMAIL_HOST_USER
from django.utils import timezone
from datetime import timedelta


@shared_task(name="course.tasks.update_course_content")
def update_course_content(course_id):
    """Sending notification about course's updates."""
    course = Course.objects.get(id=course_id)
    subject = "Email message"
    message = f"Произошло обновление курса {course.title}"
    from_email = EMAIL_HOST_USER
    subscriptions = Subscription.objects.filter(course=course_id).only("user")
    users_id = [user["user_id"] for user in subscriptions.values()]
    emails = [user["email"] for user in User.objects.filter(pk__in=users_id).values()]
    send_mail(subject, message, from_email, recipient_list=emails)


@shared_task(name="course.tasks.delete_inactive_users")
def delete_inactive_users():
    """Checks and deactivate inactive users whose last login was greater than 30 days."""
    current_date = timezone.now()
    inactive_users = User.objects.only(
        "last_login", "is_active", "is_superuser"
    ).filter(
        is_active=True,
        is_superuser=False,
        last_login__lt=current_date - timezone.timedelta(days=30),
    )
    for user in inactive_users:
        user.is_active = False
    User.objects.bulk_update(inactive_users, ["is_active"])
