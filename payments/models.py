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

    class PaymentStatus(models.TextChoices):
        SUCCESSFUL = "Успешно"
        UNSUCCESSFUL = "Не успешно"
        IN_PROCESS = "В обработке"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_payments",
        verbose_name="пользователь",
        **NULLABLE
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_payments",
        verbose_name="оплаченный курс",
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
        max_length=15,
        choices=PaymentMethod.choices,
        verbose_name="способ оплаты",
        default=PaymentMethod.TRANSFER,
    )
    payment_link = models.URLField(max_length=400, **NULLABLE)
    payment_status = models.CharField(
        max_length=12, choices=PaymentStatus.choices, default=PaymentStatus.IN_PROCESS
    )
    session_id = models.CharField(max_length=200, **NULLABLE)

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
        ordering = ["-payment_date"]
        indexes = [
            models.Index(fields=["paid_course", "paid_lesson", "payment_method"])
        ]
