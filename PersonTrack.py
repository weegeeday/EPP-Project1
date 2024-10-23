from ultralytics import YOLO
import cv2
import Send2Ardui
import TommyS2A


model = YOLO("./yolov8n.pt")  # load an official detection model
model.classes = [1]  # only detect human

while True:
    # Capture image from webcam
    cap = cv2.VideoCapture(2) #take frame from camera
    ret, img = cap.read() #read frame and store in img
    results = model(source=img, conf=0.8) #run YOLOV8 model on img
    cap.release() #stop using the camera 
    for det in results: #for each detection in results
        boxesxy = det.boxes.xyxy  # Bounding box coordinates
        try:
            x1, y1, x2, y2 = boxesxy[0] #the coords go into these vars for seperation
            direction = [int(round(float((x1 + x2)/2),1)), int(round(float((y1 + y2)/2)))] #find the middle of the box
            print(f"Coordinates: {x1}, {y1}, {x2}, {y2}") #debugging print thats useful
        except IndexError:
            print("No human detected") #self explanatory
    try:
        angles = TommyS2A.pixelToAngle(direction[0], direction[1]) #the servo angles are calculated by the pixelToAngle function.
        Send2Ardui.Send2Ardui.Send(angles) #send the angles to the arduino
        print(angles)
    except NameError:
        print("NameError") #self explanatory, happened sometimes in testing. 