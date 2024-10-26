from .serializers import UserSerializer
from rest_framework import generics
from users.models import User


class UserCreateView(generics.CreateAPIView):

    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(generics.DestroyAPIView):

    queryset = User.objects.all()