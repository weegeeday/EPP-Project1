from ultralytics import YOLO
model = YOLO("./yolov8n.pt")  # load an official detection model
results = model.track(source=2, show=True)  # source=0 to use the webcam