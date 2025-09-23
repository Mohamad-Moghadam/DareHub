from .models import Challenge, Progression
from rest_framework import serializers


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['title', 'description', 'created_at', 'updated_at', 'users', 'creator']
        extra_kwargs = {'title': {'required': True}, 'created_at': {'read_only': True}, 'updated_at': {'read_only': True}, 'creator': {'read_only': True}}

class ProgressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progression
        fields = ['challenge', 'user', 'completed', 'created_at', 'updated_at']
        extra_kwargs = {'challenge': {'read_only': True}, 'user': {'read_only': True}, 'created_at': {'read_only': True}, 'updated_at': {'read_only': True}}