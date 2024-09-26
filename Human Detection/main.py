from ultralytics import YOLO
import cv2

model = YOLO("./Human Detection/yolov8n.pt")  # load an official detection model
model.classes = [1]  # only detect human


while True:
    # Capture image from webcam
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    cap.release()
    results = model(source=img, conf=0.8)
    for det in results:
        boxesxy = det.boxes.xyxy  # Bounding box coordinates
        try:
            x1, y1, x2, y2 = boxesxy[0]
            print(f"Coordinates: {x1}, {y1}, {x2}, {y2}")
        except IndexError:
            print("No human detected")
