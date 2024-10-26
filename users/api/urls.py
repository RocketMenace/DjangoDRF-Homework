from django.urls import path

from users.apps import UsersConfig
from .views import (
    UserCreateAPIView,
    UserListAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    PaymentCreateAPIView,
    PaymentListAPIView,
    PaymentDetailAPIView,
    PaymentUpdateAPIView,
    PaymentDeleteAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    # Users urls
    path("create/", UserCreateAPIView.as_view(), name="create_user"),
    path("", UserListAPIView.as_view(), name="list_users"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="detail_users"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update_users"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete_users"),
    # Payments urls
    path("payments/create/", PaymentCreateAPIView.as_view(), name="create_payments"),
    path("payments/", PaymentListAPIView.as_view(), name="list_payments"),
    path("payments/<int:pk>/", PaymentDetailAPIView.as_view(), name="detail_payments"),
    path(
        "payments/update/<int:pk>/",
        PaymentUpdateAPIView.as_view(),
        name="update_payments",
    ),
    path(
        "payments/delete/<int:pk>/",
        PaymentDeleteAPIView.as_view(),
        name="delete_payments",
    ),
]
