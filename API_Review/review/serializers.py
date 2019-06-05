from django.conf import settings
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.Serializer):
    user = serializers.CharField()
    score = serializers.IntegerField()
    review = serializers.CharField(max_length=255)
