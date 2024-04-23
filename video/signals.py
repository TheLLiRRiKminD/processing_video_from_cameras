from django.db.models.signals import post_save
from django.dispatch import receiver
from config import settings
from video.models import Video
from video_frame.models import VideoFrame
import cv2
import os


@receiver(post_save, sender=Video)
def create_processed_frames(sender, instance, created, **kwargs):
    if created:
        output_path = os.path.join(settings.MEDIA_ROOT, 'frames', str(instance.id))
        os.makedirs(output_path, exist_ok=True)

        cap = cv2.VideoCapture(instance.video_file.path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        frames = []
        success, frame = cap.read()
        frame_number = 0
        while success and len(frames) < frame_count:
            frames.append(frame)
            frame_number += 1
            success, frame = cap.read()

        for i, frame in enumerate(frames):
            if frame_number % (fps // 5) == 0:
                # Сохранить кадр
                frame_path = os.path.join(output_path, f'frame-{frame_number}.jpg')
                cv2.imwrite(frame_path, frame)

                # Создать объект VideoFrames
                VideoFrame.objects.create(
                    Video=instance,
                    frame_image=frame_path
                )
