from django.urls import path

from users.apps import UsersConfig
from .views import (
    UserCreateView,
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create_user"),
    path("", UserListView.as_view(), name="list_users"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail_users"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="update_users"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="delete_users"),
]