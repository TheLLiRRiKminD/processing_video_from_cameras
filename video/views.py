import os
import time
import cv2
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def create(self, request, **kwargs):
        try:
            rtsp_url = os.getenv('RTSP_CAMERA_URL')
            cap = cv2.VideoCapture(rtsp_url)

            if not cap.isOpened():
                return Response({'error': 'Ошибка открытия камеры'}, status=500)

            frame_count = 0
            fps = 5
            interval = 1 / fps
            start_time = time.time()

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Применяем медианный фильтр для удаления шума
                frame = cv2.medianBlur(frame, 5)

                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time >= interval:
                    video = Video(name='Video Stream')
                    video.video_file.save(f'video_frame_{frame_count}.jpg', frame, save=True)
                    frame_count += 1
                    start_time = time.time()

            return Response({'message': 'Кадры видео сохранены и обработаны для удаления шума'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
