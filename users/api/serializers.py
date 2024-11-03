from rest_framework import serializers
from users.models import User
from payments.api.serializers import PaymentSerializer


class UserSerializer(serializers.ModelSerializer):

    user_payments = PaymentSerializer(read_only=True, many=True)

    class Meta:

        model = User
        fields = "__all__"

class UserPrivateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "city"]
