from django.db.models.signals import post_save
from django.dispatch import receiver
from config import settings
from video.models import Video
from video_frame.models import VideoFrame
import cv2


@receiver(post_save, sender=Video)
def create_processed_frames(instance, created, fps=5, **kwargs):
    """
    Считывает кадры из видео со скоростью fps, удаляет шум и сохраняет дешумленные кадры.
    """
    if created:
        # Открыть объект видеозахвата
        cap = cv2.VideoCapture(instance.video_file.path)

        # Проверить, открыт ли объект видеозахвата
        if not cap.isOpened():
            print("Не удалось открыть видеофайл.")
            return

        # Создать каталог для сохранения дешумленных кадров
        import os
        output_path = os.path.join(settings.MEDIA_ROOT, 'frames', str(instance.id))
        os.makedirs(output_path, exist_ok=True)

        # Скорость считывания кадров видео
        video_fps = cap.get(cv2.CAP_PROP_FPS)

        # Интервал между сохраняемыми кадрами (в кадрах)
        frame_interval = int(video_fps / fps)

        # Счетчик кадров
        frame_count = 0

        # Цикл для чтения кадров
        while True:
            # Читать следующий кадр
            success, frame = cap.read()
            if not success:
                break

            # Сохранять кадр только в том случае, если счетчик кадров кратен интервалу между кадрами
            if frame_count % frame_interval == 0:
                # Удалить шум из кадра
                denoised_frame = cv2.GaussianBlur(frame, (5, 5), 0)

                # Сохранить дешумленный кадр
                cv2.imwrite(os.path.join(output_path, f"frame_{frame_count}.jpg"), denoised_frame)

            # Увеличить счетчик кадров
            frame_count += 1

            VideoFrame.objects.create(
                video=instance,
                frame_image=output_path,
            )

        # Освободить объект видеозахвата
        cap.release()
