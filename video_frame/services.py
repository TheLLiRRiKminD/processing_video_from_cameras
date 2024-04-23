import cv2


def remove_noise_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Применяем фильтр Гаусса для удаления шумов
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        frames.append(frame)

    cap.release()

    return frames
