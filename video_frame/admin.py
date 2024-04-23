from django.contrib import admin

from video_frame.models import VideoFrame


@admin.register(VideoFrame)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'video', 'timestamp',)
