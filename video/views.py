from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Video и создания подключения к камере
    В тело запроса передается параметр id ссылки на камеру
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
