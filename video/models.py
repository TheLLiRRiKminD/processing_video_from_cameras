from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
