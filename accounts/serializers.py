from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 
        'last_name', 'phone_number', 'revenue',
        'pending_payments',
        'is_staff', 
        'admin'
        ]