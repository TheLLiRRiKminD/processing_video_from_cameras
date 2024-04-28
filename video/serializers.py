from rest_framework import serializers
from .models import Video, RTSUrl


class VideoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Video
    """
    class Meta:
        model = Video
        fields = '__all__'


class RTSUrlSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели RTSUrl
    """
    class Meta:
        model = RTSUrl
        fields = '__all__'
