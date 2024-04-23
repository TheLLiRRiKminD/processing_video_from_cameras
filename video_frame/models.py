from django.db import models

from video.models import Video


# Create your models here.


class VideoFrame(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    frame_image = models.ImageField(upload_to='videos_frame/')
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Frame {self.id} of {self.video}"

    class Meta:
        verbose_name = 'Video Frame'
        verbose_name_plural = 'Video Frames'
