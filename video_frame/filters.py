import django_filters
from video_frame.models import VideoFrame


class DateCreatedFilter(django_filters.Filter):
    def filter(self, queryset, value):
        if value is not None:
            date_from, date_to = value.split(',')
            return queryset.filter(created_at__gte=date_from, created_at__lte=date_to)
        return queryset


class VideoFrameFilter(django_filters.FilterSet):
    date_created = DateCreatedFilter()

    class Meta:
        model = VideoFrame
        fields = ['date_created']
