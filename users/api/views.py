from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [
        AllowAny,
    ]

    def perform_create(self, serializer):
        serializer.validated_data["password"] = make_password(
            serializer.validated_data.get("password")
        )
        serializer.save()


class UserListAPIView(generics.ListAPIView):

    queryset = User.objects.prefetch_related("user_payments").all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(generics.DestroyAPIView):

    queryset = User.objects.all()
