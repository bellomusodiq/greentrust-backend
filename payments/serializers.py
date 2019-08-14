from rest_framework import serializers
from .models import Payment, Revenue, Witdrawal

class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = "__all__"

        
class WitdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Witdrawal
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

