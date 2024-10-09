from ultralytics import YOLO
import cv2
try:
    import Send2Ardui
except ImportError:
    print("bruh")
import TommyS2A


model = YOLO("./yolov8n.pt")  # load an official detection model
model.classes = [1]  # only detect human

while True:
    # Capture image from webcam
    cap = cv2.VideoCapture(2)
    ret, img = cap.read()
    results = model(source=img, conf=0.8)
    cap.release()
    for det in results:
        boxesxy = det.boxes.xyxy  # Bounding box coordinates
        try:
            x1, y1, x2, y2 = boxesxy[0]
            direction = [int(round(float((x1 + x2)/2),1)), int(round(float((y1 + y2)/2)))]
            print(f"Coordinates: {x1}, {y1}, {x2}, {y2}")
        except IndexError:
            print("No human detected")
    try:
        angles = TommyS2A.pixelToAngle(direction[0], direction[1])
        Send2Ardui.Send2Ardui.Send(angles)
        print(angles)
    except NameError:
        print("NameError")