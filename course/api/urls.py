from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from .views import (
    LessonListAPIView,
    LessonDetailAPIView,
    LessonCreateAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    CourseViewSet,
    SubscriptionAPIView,
)

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    # Lessons urls.
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lessons/", LessonListAPIView.as_view(), name="lessons"),
    path("lessons/<int:pk>", LessonDetailAPIView.as_view(), name="lesson_detail"),
    path(
        "lessons/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path(
        "lessons/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    # Subscriptions urls.
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
] + router.urls
