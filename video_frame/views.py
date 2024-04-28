from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import VideoFrameFilter
from .models import VideoFrame
from .serializers import VideoFrameSerializer


class VideoFrameViewSet(viewsets.ModelViewSet):
    """
    Представление для получения кадров из базы данных
    """
    queryset = VideoFrame.objects.all()
    serializer_class = VideoFrameSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_class = VideoFrameFilter
