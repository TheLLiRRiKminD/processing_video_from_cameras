from rest_framework.routers import DefaultRouter
from video.apps import VideoConfig
from video_frame.views import VideoFrameViewSet

app_name = VideoConfig.name

router = DefaultRouter()
router.register(r'', VideoFrameViewSet, basename='Video_frame')

urlpatterns = router.urls
