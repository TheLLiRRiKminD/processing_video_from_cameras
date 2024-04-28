from video.apps import VideoConfig
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet, RTSUrlViewSet

app_name = VideoConfig.name

router = DefaultRouter()
router.register(r'', VideoViewSet, basename='Video')
router.register(r'RTSurl', RTSUrlViewSet, basename='RTS')

urlpatterns = router.urls
