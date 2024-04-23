import cv2
import os


def capture_and_process_frames(output_path, fps=5):
    """Захватывает видеопоток, обрабатывает кадры с помощью OpenCV и сохраняет их в указанном выходном пути.

    Args:
        output_path (str): Путь к выходному каталогу для сохранения кадров.
        fps (int, optional): Частота сохранения кадров (по умолчанию 5).
    """

    # Захват видеопотока
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, fps)

    # Обработка и сохранение кадров
    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Обработка кадра (например, удаление шума)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.medianBlur(frame, 5)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        # Сохранение кадра
        cv2.imwrite(os.path.join(output_path, f'frame-{frame_count}.jpg'), frame)
        frame_count += 1

    # Освобождение ресурсов
    cap.release()
    cv2.destroyAllWindows()
