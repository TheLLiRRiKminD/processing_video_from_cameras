import django_filters
from video_frame.models import VideoFrame


class VideoFrameFilter(django_filters.FilterSet):
    date_range = django_filters.DateFromToRangeFilter(field_name='created_at')

    class Meta:
        model = VideoFrame
        fields = ['date_range']
