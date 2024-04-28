from django.db import models


class Video(models.Model):
    """
    Модель Video
    """
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    RTSUrl = models.ForeignKey('RTSUrl', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'


class RTSUrl(models.Model):
    """
    Модель для добавления нескольких адресов камер
    """
    URL = models.CharField(max_length=500)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.URL

    class Meta:
        verbose_name = 'RTSUrl'
        verbose_name_plural = 'RTSUrls'
