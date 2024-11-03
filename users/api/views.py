from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from users.permissions import IsOwner
from users.models import User
from .serializers import UserSerializer, UserPrivateSerializer


class UserCreateAPIView(generics.CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.validated_data["password"] = make_password(
            serializer.validated_data.get("password")
        )
        serializer.save()


class UserListAPIView(generics.ListAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return User.objects.prefetch_related("user_payments").all()
        elif user.is_authenticated:
            self.serializer_class = UserPrivateSerializer
            return User.objects.all()
        return User.objects.none()


class UserDetailAPIView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user != self.get_object():
            return UserPrivateSerializer
        return UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserDeleteAPIView(generics.DestroyAPIView):

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
