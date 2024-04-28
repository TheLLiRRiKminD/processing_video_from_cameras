from rest_framework import serializers
from .models import VideoFrame


class VideoFrameSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели RTSUrl
    """
    class Meta:
        model = VideoFrame
        fields = '__all__'
