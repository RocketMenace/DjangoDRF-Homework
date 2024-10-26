from django.db import models

# Create your models here.

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    preview = models.ImageField(upload_to="course/", verbose_name="превью", **NULLABLE)
    description = models.TextField(verbose_name="описание")

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
    link = models.URLField(verbose_name="ссылка на урок")
    course = models.ForeignKey(Course, related_name="lessons", verbose_name="курс", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ["title"]
        indexes = [models.Index(fields=["title"])]

    def __str__(self):
        return self.title



