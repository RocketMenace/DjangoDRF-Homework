from rest_framework import serializers
from course.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(read_only=True, many=True)
    count_lessons = serializers.SerializerMethodField(read_only=True)

    def get_count_lessons(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"
