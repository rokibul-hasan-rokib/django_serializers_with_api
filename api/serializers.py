from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if Customer.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']