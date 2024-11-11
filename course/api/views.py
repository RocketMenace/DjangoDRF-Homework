from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course.api.serializers import (
    CourseSerializer,
    LessonSerializer,
)
from course.models import Course, Lesson, Subscription
from users.permissions import IsModerator, IsOwner
from .paginators import ItemPaginator


class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated | IsModerator]

    def post(self, *args, **kwargs):

        user = self.request.user
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)
        try:
            subscription = Subscription.objects.get(user=user, course=course)
            if subscription.status == Subscription.Status.ACTIVE:
                subscription.status = Subscription.Status.NOT_ACTIVE
                subscription.save()
                message = "Подписка отключена"
                return Response({"message": message})
            subscription.status = Subscription.Status.ACTIVE
            subscription.save()
            return Response({"message": "Подписка включена"})
        except ObjectDoesNotExist:
            Subscription.objects.create(user=user, course=course)
            return Response({"message": "Подписка включена"})


class LessonListAPIView(generics.ListAPIView):

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated | IsModerator]
    pagination_class = ItemPaginator

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.is_staff:
            return Lesson.objects.all()
        elif user.is_authenticated:
            return Lesson.objects.all().filter(owner=user.id)
        return Lesson.objects.none()


class LessonDetailAPIView(generics.RetrieveAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonCreateAPIView(generics.CreateAPIView):

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):

    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ~IsModerator]


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.prefetch_related("lessons", "status").all()
    serializer_class = CourseSerializer
    pagination_class = ItemPaginator

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [
                IsAuthenticated | IsModerator,
            ]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == "update":
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == "partial_update":
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return Course.objects.all()
        elif user.is_authenticated:
            return Course.objects.all().filter(owner=user.id)
        return Course.objects.none()
