import cv2

cap = cv2.VideoCapture(7)
ret, img = cap.read()
while True:
    cv2.imshow("Image", img)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
