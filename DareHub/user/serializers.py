from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'email']
        read_only_fields = ['is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}

    def  create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user