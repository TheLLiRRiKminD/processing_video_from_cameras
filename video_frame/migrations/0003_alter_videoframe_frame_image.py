# Generated by Django 5.0.4 on 2024-04-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_frame', '0002_alter_videoframe_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoframe',
            name='frame_image',
            field=models.FileField(upload_to='videos_frame/'),
        ),
    ]
