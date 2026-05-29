from ultralytics import YOLO
import cv2
import time

# Load YOLO model
model = YOLO("yolov8n.pt")

prev_time = 0

def process_frame(frame):

    global prev_time

    # Run detection
    results = model(frame)

    # Draw results
    annotated_frame = results[0].plot()

    # FPS Calculation
    current_time = time.time()

    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0

    prev_time = current_time

    # Display FPS
    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    return annotated_frame