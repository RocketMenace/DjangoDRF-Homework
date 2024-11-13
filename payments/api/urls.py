from django.urls import path

from payments.apps import PaymentsConfig
from .views import (
    PaymentCreateAPIView,
    PaymentListAPIView,
    PaymentDetailAPIView,
    PaymentUpdateAPIView,
    PaymentDeleteAPIView,
    PaymentStatusUpdateView
)

app_name = PaymentsConfig.name

urlpatterns = [
    # Payments urls
    path("create/", PaymentCreateAPIView.as_view(), name="create_payments"),
    path("", PaymentListAPIView.as_view(), name="list_payments"),
    path("<int:pk>/", PaymentDetailAPIView.as_view(), name="detail_payments"),
    path(
        "update/<int:pk>/",
        PaymentUpdateAPIView.as_view(),
        name="update_payments",
    ),
    path(
        "delete/<int:pk>/",
        PaymentDeleteAPIView.as_view(),
        name="delete_payments",
    ),
    path("success/", PaymentStatusUpdateView.as_view(), name="success")
]
