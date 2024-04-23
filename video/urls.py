from video.apps import VideoConfig

from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

app_name = VideoConfig.name

router = DefaultRouter()
router.register(r'', VideoViewSet, basename='Video')

urlpatterns = router.urls
