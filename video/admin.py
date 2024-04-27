from django.contrib import admin

from video.models import Video, RTSUrl


@admin.register(Video)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)


@admin.register(RTSUrl)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'URL')
