from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Witdrawal, Revenue, Payment
from .serializers import WitdrawalSerializer, RevenueSerializer, PaymentSerializer
# Create your views here.

class RevenueViewSet(ModelViewSet):
    queryset = Revenue.objects.all()[:10]
    serializer_class = RevenueSerializer

class WitdrawalViewSet(ModelViewSet):
    queryset = Witdrawal.objects.all()
    serializer_class = WitdrawalSerializer

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer