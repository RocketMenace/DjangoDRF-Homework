from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

NULLABLE = {"null": True, "blank": True}
User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    preview = models.ImageField(upload_to="course/", verbose_name="превью", **NULLABLE)
    description = models.TextField(verbose_name="описание")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="владелец",
        related_name="courses_owner",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ["title"]
        indexes = [models.Index(fields=["title"])]

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name="предмет")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(upload_to="lessons/", verbose_name="превью", **NULLABLE)
    link = models.CharField(max_length=200, verbose_name="ссылка на урок")
    course = models.ForeignKey(
        Course, related_name="lessons", verbose_name="курс", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="владелец",
        related_name="lessons_owner",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ["title"]
        indexes = [models.Index(fields=["title"])]

    def __str__(self):
        return self.title


class Subscription(models.Model):

    class Status(models.TextChoices):

        ACTIVE = "активна"
        NOT_ACTIVE = "не активна"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscribers",
        verbose_name="подписчик",
        **NULLABLE,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        verbose_name="курс",
        **NULLABLE,
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
        verbose_name="статус",
    )

    class Meta:

        verbose_name = "подписка"
        verbose_name_plural = "подписки"

    def __str__(self):
        return f"{self.user} {self.course} {self.status}"
