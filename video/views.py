from django.shortcuts import get_object_or_404
import ffmpeg
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
import cv2
from video.models import RTSUrl, Video
from video.serializers import VideoSerializer, RTSUrlSerializer
import numpy as np
from video_frame.models import VideoFrame


class VideoViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Video и создания подключения к камере
    В тело запроса передается параметр id ссылки на камеру
    """
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, **kwargs):
        try:
            rtsp_id = request.data.get('RTSUrl_id')
            if rtsp_id is None:
                return Response({"message": "Отсутствует идентификатор камеры в запросе"}, status=400)
            camera = get_object_or_404(RTSUrl, id=rtsp_id)

            process = (
                ffmpeg
                .input(camera.URL, rtsp_transport='tcp',
                       timeout=0)  # Устанавливаем время ожидания в 0 для бесконечного ожидания
                .output('pipe:', format='rawvideo', pix_fmt='bgr24')
                .run_async(pipe_stdout=True)
            )

            frame_count = 0

            while True:
                in_bytes = process.stdout.read(1920 * 1080 * 3)  # Размер кадра для Full HD
                if not in_bytes:
                    break

                frame = np.frombuffer(in_bytes, np.uint8).reshape([1080, 1920, 3])  # Размер кадра для Full HD

                # Применяем медианный фильтр для удаления шума
                frame = cv2.medianBlur(frame, 5)

                VideoFrame.objects.create(
                    name=f'video_frame_{frame_count}.jpg',
                    frame=frame,
                )

                frame_count += 1

            return Response({'message': 'Кадры видео сохранены и обработаны для удаления шума'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class RTSUrlViewSet(viewsets.ModelViewSet):
    """
    Представление для добавления в базу ссылок на RTS камеры
    """
    queryset = RTSUrl.objects.all()
    serializer_class = RTSUrlSerializer
    permission_classes = [IsAuthenticated]
