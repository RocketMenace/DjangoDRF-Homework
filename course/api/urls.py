from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from .views import (
    LessonListView,
    LessonDetailView,
    LessonCreateView,
    LessonUpdateView,
    LessonDestroyView,
    CourseViewSet,
)

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    # Lessons urls.
    path("lessons/create/", LessonCreateView.as_view(), name="lesson_create"),
    path("lessons/", LessonListView.as_view(), name="lessons"),
    path("lessons/<int:pk>", LessonDetailView.as_view(), name="lesson_detail"),
    path("lessons/update/<int:pk>/", LessonUpdateView.as_view(), name="lesson_update"),
    path("lessons/delete/<int:pk>/", LessonDestroyView.as_view(), name="lesson_delete"),
] + router.urls