from rest_framework import serializers
from .models import VideoFrame


class VideoFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFrame
        fields = '__all__'
