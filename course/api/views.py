from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from course.api.serializers import CourseSerializer, LessonSerializer
from course.models import Course, Lesson
from users.permissions import IsModerator, IsOwner


class LessonListAPIView(generics.ListAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator]


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
    permission_classes = [IsOwner & IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.prefetch_related("lessons").all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [
                IsAuthenticated & IsModerator,
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
