from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


# Create your tests here.


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            password="qwerasdf123",
            email="test_123@gmail.com",
            phone="45267724832",
            city="Denver",
        )
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        url = reverse("users:register")
        data = {
            "password": "qwerasdf123",
            "email": "test_1234@gmail.com",
            "phone": "452677248325",
            "city": "Denver",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_retrieve(self):
        url = reverse("users:detail_users", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), self.user.email)

    def test_user_update(self):
        url = reverse("users:update_users", args=(self.user.pk,))
        data = {
            "password": "qwerasdf123",
            "email": "test_1234@gmail.com",
            "phone": "452677248325",
            "city": "New York",
        }
        response = self.client.patch(url, data)
        response_data = response.json()
        self.assertEqual(response_data.get("city"), "New York")

    def test_user_delete(self):
        url = reverse("users:delete_users", args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)

    def test_user_list(self):
        url = reverse("users:list_users")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
