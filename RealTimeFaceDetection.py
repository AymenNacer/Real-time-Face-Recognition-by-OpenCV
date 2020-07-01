import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) # for webcam



while (True):
    ret, vid = cap.read()
    faces = face_cascade.detectMultiScale(vid, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (255, 255, 0), 2) # to draw a rectangle around the face
    cv2.imshow('WebCam', vid)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()
