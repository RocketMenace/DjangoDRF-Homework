from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Lesson, Course, Subscription
from users.models import User


# Create your tests here.


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            password="qwerasdf123",
            email="test_123@gmail.com",
            phone="45267724832",
            city="Denver",
        )
        self.course = Course.objects.create(
            title="Demo course", description="Demo description", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Demo lesson",
            description="Demo description",
            link="https://www.youtube.com",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse("course:lesson_create")
        data = {
            "title": "Demo lesson",
            "description": "Demo description",
            "link": "https://www.youtube.com",
            "course": self.course.pk,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        # self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_lesson_retrieve(self):
        url = reverse("course:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_update(self):
        url = reverse("course:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Another lesson",
            "description": "Demo description",
            "link": "https://www.youtube.com",
            "course": self.course.pk,
            "owner": self.user.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(data.get("title"), "Another lesson")

    def test_lesson_delete(self):
        url = reverse("course:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("course:lessons")
        response = self.client.get(url)
        result = response.json()
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "title": self.lesson.title,
                    "description": self.lesson.description,
                    "preview": None,
                    "link": "https://www.youtube.com",
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class LessonAuthorizeTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            password="qwerasdf123",
            email="test_123@gmail.com",
            phone="45267724832",
            city="Denver",
        )
        self.course = Course.objects.create(
            title="Demo course", description="Demo description", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Demo lesson",
            description="Demo description",
            link="https://www.youtube.com",
            course=self.course,
            owner=self.user,
        )

    def test_lesson_create(self):
        url = reverse("course:lesson_create")
        data = {
            "title": "Demo lesson",
            "description": "Demo description",
            "link": "https://www.youtube.com",
            "course": self.course.pk,
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_retrieve(self):
        url = reverse("course:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_update(self):
        url = reverse("course:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Another lesson",
            "description": "Demo description",
            "link": "https://www.youtube.com",
            "course": self.course.pk,
            "owner": self.user.pk,
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_delete(self):
        url = reverse("course:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_list(self):
        url = reverse("course:lessons")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class LessonIsOwnerTestCase(APITestCase):
    def setUp(self):
        self.owner = User.objects.create(
            password="qwerasdf123",
            email="test_1234@gmail.com",
            phone="452677245832",
            city="Denver",
        )
        self.user = User.objects.create(
            password="qwerasdf123",
            email="test_123@gmail.com",
            phone="45267724832",
            city="Denver",
        )
        self.course = Course.objects.create(
            title="Demo course", description="Demo description", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Demo lesson",
            description="Demo description",
            link="https://www.youtube.com",
            course=self.course,
            owner=self.owner,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("course:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_lesson_update(self):
        url = reverse("course:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Another lesson",
            "description": "Demo description",
            "link": "https://www.youtube.com",
            "course": self.course.pk,
            "owner": self.user.pk,
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_lesson_delete(self):
        url = reverse("course:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            password="qwerasdf123",
            email="test_123@gmail.com",
            phone="45267724832",
            city="Denver",
        )
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title="Demo course", description="Demo description", owner=self.user
        )

    def test_course_create(self):

        url = "http://127.0.0.1:8000/course/"
        data = {
            "title": "Demo course",
            "description": "Demo description",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_retrieve(self):

        url = reverse("course:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.course.title)

    def test_course_delete(self):

        url = reverse("course:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        url = reverse("course:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            password="qwerasdf123",
            email="test_123@gmail.com",
            phone="45267724832",
            city="Denver",
        )
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title="Demo course", description="Demo description", owner=self.user
        )
        self.status = Subscription.Status.ACTIVE
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course, status=self.status
        )

    def test_subscription_create(self):
        url = reverse("course:subscription")
        data = {"user": self.user.pk, "course": self.course.pk, "status": self.status}
        response = self.client.post(url, data)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 1)
        self.assertEqual(response_data.get("message"), "Подписка отключена")
        response = self.client.post(url, data)
        response_data = response.json()
        self.assertEqual(response_data.get("message"), "Подписка включена")
