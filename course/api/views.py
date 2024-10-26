from rest_framework import generics, viewsets
from course.models import Course, Lesson
from course.api.serializers import CourseSerializer, LessonSerializer


class LessonListView(generics.ListAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailView(generics.RetrieveAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateView(generics.CreateAPIView):

    serializer_class = LessonSerializer


class LessonUpdateView(generics.UpdateAPIView):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyView(generics.DestroyAPIView):

    queryset = Lesson.objects.all()


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer