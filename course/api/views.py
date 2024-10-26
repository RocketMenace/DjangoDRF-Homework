from rest_framework import generics, viewsets
from course.models import Course, Lesson
from course.api.serializers import CourseSerializer, LessonSerializer


class LessonListAPIView(generics.ListAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailAPIView(generics.RetrieveAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):

    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):

    queryset = Lesson.objects.all()


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer