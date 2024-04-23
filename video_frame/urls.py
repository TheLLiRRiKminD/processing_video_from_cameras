from django.urls import path, include
from rest_framework import routers

from video import apps
from video_frame.views import VideoFrameViewSet

app_name = apps.VideoConfig

router = routers.DefaultRouter()
router.register(r'videos_frame', VideoFrameViewSet)

urlpatterns = [
    path('videos_frame/', include(router.urls)),
]
