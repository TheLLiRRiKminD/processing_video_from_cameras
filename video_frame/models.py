from django.db import models

from video.models import Video


class VideoFrame(models.Model):
    """
    Модель для сохранения кадров
    """
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    frame_image = models.ImageField(upload_to='videos_frame/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Frame {self.id} of {self.video}"

    class Meta:
        verbose_name = 'Video Frame'
        verbose_name_plural = 'Video Frames'
