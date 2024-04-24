from django.apps import AppConfig
from django.core.signals import request_finished


class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'

    # def ready(self):
    #     import video.signals
    #     request_finished.connect(video.signals.create_processed_frames)
