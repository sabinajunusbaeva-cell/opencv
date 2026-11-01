import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

if not cap:
    print("Camera not found")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Камера жок")
        break

    cv2.putText(frame,'Python50',(250,20),
                cv2.FONT_HERSHEY_SIMPLEX,1,(222,222,222),1)

    cv2.putText(frame,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(10,20),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)

    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()