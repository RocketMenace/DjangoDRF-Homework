from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from .views import (
    UserCreateAPIView,
    UserListAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    # Token urls
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=[AllowAny]),
        name="login",
    ),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    # Users urls
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="list_users"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="detail_users"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update_users"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete_users"),
]
