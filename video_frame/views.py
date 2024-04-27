from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .filters import VideoFrameFilter
from .models import VideoFrame
from .serializers import VideoFrameSerializer


class VideoFrameViewSet(viewsets.ModelViewSet):
    queryset = VideoFrame.objects.all()
    serializer_class = VideoFrameSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = VideoFrameFilter
