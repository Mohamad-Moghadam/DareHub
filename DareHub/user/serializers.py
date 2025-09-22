from .models import customUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ['username', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'email' ,'phone_number']
        read_only_fields = ['is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def  create(self, validated_data):
        password = validated_data.pop('password')
        user = customUser(**validated_data)
        user.set_password(password)
        user.save()
        return user