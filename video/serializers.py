from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Video
    """
    class Meta:
        model = Video
        fields = '__all__'
