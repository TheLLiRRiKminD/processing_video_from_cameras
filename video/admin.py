from django.contrib import admin

from video.models import Video


@admin.register(Video)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)