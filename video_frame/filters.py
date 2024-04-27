from datetime import datetime
import django_filters
from rest_framework.response import Response
from video_frame.models import VideoFrame
from rest_framework import status


class DateCreatedFilter(django_filters.Filter):
    def filter(self, queryset, value):
        if value is not None:
            try:
                date_from, date_to = value.split(',')
                date_from = datetime.strptime(date_from, '%Y-%m-%d %H:%M:%S').date()
                date_to = datetime.strptime(date_to, '%Y-%m-%d %H:%M:%S').date()
                return queryset.filter(created_at__gte=date_from, created_at__lte=date_to)
            except ValueError:
                raise Response({"error": "Invalid date format. Expected YYYY-MM-DD HH:MM:SS"},
                               status=status.HTTP_400_BAD_REQUEST)
        return queryset


class VideoFrameFilter(django_filters.FilterSet):
    date_created = DateCreatedFilter()

    class Meta:
        model = VideoFrame
        fields = ['date_created']
