from datetime import datetime
import django_filters
from django.core.exceptions import BadRequest
from video_frame.models import VideoFrame


class DateCreatedFilter(django_filters.Filter):
    """
    Фильтр для кадров из потока по дате создания
    """
    def filter(self, queryset, value):
        if value is not None:
            try:
                date_from, date_to = value.split(',')
                date_from = datetime.strptime(date_from, '%Y-%m-%d %H:%M:%S').date()
                date_to = datetime.strptime(date_to, '%Y-%m-%d %H:%M:%S').date()
                return queryset.filter(created_at__gte=date_from, created_at__lte=date_to)
            except ValueError:
                raise BadRequest("Неверный формат даты, попробуйте YYYY-MM-DD HH:MM:SS")
        return queryset


class VideoFrameFilter(django_filters.FilterSet):
    date_created = DateCreatedFilter()

    class Meta:
        model = VideoFrame
        fields = ['date_created']
