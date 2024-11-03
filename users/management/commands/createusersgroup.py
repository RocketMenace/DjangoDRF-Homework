from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        group = Group(name="Пользователи")
        group.save()
        can_view_lessons = Permission.objects.get(name="Can view урок")
        can_edit_lessons = Permission.objects.get(name="Can change урок")
        can_view_courses = Permission.objects.get(name="Can view курс")
        can_edit_courses = Permission.objects.get(name="Can change курс")
        group.permissions.set(
            [
                can_view_lessons,
                can_edit_lessons,
                can_view_courses,
                can_edit_courses,
            ]
        )
