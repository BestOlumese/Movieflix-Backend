from rest_framework import serializers
from .models import Newsletter

class NewsletterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=500)
    def create(self, validated_data):
        return Newsletter.objects.create(**validated_data)