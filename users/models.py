from django.db import models
from django.contrib.auth.models import AbstractUser
from course.models import Lesson, Course

# Create your models here.

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    phone = models.CharField(max_length=20, verbose_name="номер телефона", unique=True)
    city = models.CharField(max_length=100, verbose_name="город")
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = "наличная оплата"
        TRANSFER = "перевод на счет"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_payments",
        verbose_name="пользователь",
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_payments",
        verbose_name="оплаченный курс",
        **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lesson_payments",
        verbose_name="оплаченный  урок",
        **NULLABLE
    )
    amount_paid = models.PositiveIntegerField(verbose_name="сумма оплаты")
    payment_method = models.CharField(
        max_length=15, choices=PaymentMethod.choices, verbose_name="способ оплаты"
    )

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
        ordering = ["-payment_date"]
