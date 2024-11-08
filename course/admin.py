from django.contrib import admin
from course.models import Course, Lesson, Subscription

# Register your models here.


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ["id", "title", "description"]
    list_filter = ["title"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = ["id", "title", "description", "link", "course"]
    list_filter = ["title"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "course", "status"]
