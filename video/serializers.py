from rest_framework import serializers
from .models import Video, RTSUrl


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class RTSUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = RTSUrl
        fields = '__all__'
