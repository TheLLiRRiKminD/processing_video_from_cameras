# Generated by Django 5.0.4 on 2024-04-28 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_alter_rtsurl_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_file',
        ),
    ]
