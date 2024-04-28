from celery import shared_task
from datetime import datetime, timedelta
from video.models import Video


@shared_task
def delete_old_videos_task():
    """
    Периодическая задача для удаления старых видео, которые хранятся в базе более 30 дней
    """
    one_month_ago = datetime.now() - timedelta(days=30)
    old_videos = Video.objects.filter(created_at__lt=one_month_ago)
    for video in old_videos:
        video.delete()
