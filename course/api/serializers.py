from rest_framework import serializers
from course.validators import LinkValidator
from course.models import Course, Lesson, Subscription
from django.core.exceptions import ObjectDoesNotExist


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            LinkValidator(field="link"),
        ]


class CourseSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(read_only=True, many=True)
    count_lessons = serializers.SerializerMethodField(read_only=True)
    subscription_status = serializers.SerializerMethodField(read_only=True)

    def get_subscription_status(self, obj):
        request = self.context.get("request")
        try:
            return obj.subscriptions.get(course=obj.id).status
        except ObjectDoesNotExist:
            obj.subscriptions.create(
                user=request.user,
                course=obj.id,
                status=Subscription.Status.NOT_ACTIVE,
            )
            return obj.subscriptions.get(course=obj.id).status

    def get_count_lessons(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"
