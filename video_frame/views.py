from rest_framework import viewsets
from .models import VideoFrame
from .serializers import VideoFrameSerializer


class VideoFrameViewSet(viewsets.ModelViewSet):
    queryset = VideoFrame.objects.all()
    serializer_class = VideoFrameSerializer
