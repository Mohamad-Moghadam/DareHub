from .models import Challenge
from rest_framework import serializers


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['title', 'description', 'created_at', 'updated_at']
        extra_kwargs = {'title': {'required': True}, 'created_at': {'read_only': True}, 'updated_at': {'read_only': True}}