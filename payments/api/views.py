from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from payments.models import Payment
from payments.services import StripePaymentManager
from .serializers import PaymentSerializer


class PaymentCreateAPIView(generics.CreateAPIView):

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.validated_data
        payment_manager = StripePaymentManager(
            payment["amount_paid"], payment["paid_course"]
        )
        session_id, payment_link = payment_manager.process_payment()
        serializer.save(
            user=self.request.user, session_id=session_id, payment_link=payment_link
        )


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
