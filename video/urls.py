from video import apps
from django.urls import path, include
from rest_framework import routers
from .views import VideoViewSet

app_name = apps.VideoConfig

router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('video/', include(router.urls)),
]
