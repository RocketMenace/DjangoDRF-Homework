from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .serializers import PaymentSerializer
from rest_framework import generics
from payments.models import Payment
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny


class PaymentCreateAPIView(generics.CreateAPIView):

    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    ordering_fields = ("payment_date",)


class PaymentDetailAPIView(generics.RetrieveAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateAPIView(generics.UpdateAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDeleteAPIView(generics.DestroyAPIView):

    queryset = Payment.objects.all()
