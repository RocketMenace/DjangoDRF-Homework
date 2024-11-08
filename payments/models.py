from django.contrib.auth import get_user_model
from django.db import models

from course.models import Lesson, Course

# Create your models here.

NULLABLE = {"blank": True, "null": True}
User = get_user_model()


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
        indexes = [
            models.Index(fields=["paid_course", "paid_lesson", "payment_method"])
        ]
