from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
import cv2
import time
from video.models import RTSUrl, Video
from video.serializers import VideoSerializer, RTSUrlSerializer
from video_frame.models import VideoFrame


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def create(self, request, **kwargs):
        try:
            rtsp_id = request.data.get('RTSUrl_id')
            if rtsp_id is None:
                return Response({"message": "Отсутствует идентификатор камеры в запросе"}, status=400)
            camera = get_object_or_404(RTSUrl, id=rtsp_id)  # Получение ссылки на камеру по ключу
            cap = cv2.VideoCapture(camera.URL)
            if not cap.isOpened():
                return Response({'error': 'Failed to open RTSP stream'}, status=500)

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
                    VideoFrame.objects.create(
                        name=f'video_frame_{frame_count}.jpg',
                        frame_image=frame
                    )

                    frame_count += 1
                    start_time = time.time()

            return Response({'message': 'Кадры видео сохранены и обработаны для удаления шума'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class RTSUrlViewSet(viewsets.ModelViewSet):
    queryset = RTSUrl.objects.all()
    serializer_class = RTSUrlSerializer
