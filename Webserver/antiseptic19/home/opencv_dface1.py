from django.conf import settings
import cv2
import numpy as np


def opencv_dface1(path):
    #detector = cv2.CascadeClassifier('/Users/u_rim/Desktop/face_recognition/haarcascade_frontalface_default.xml')
    #다운 받은 파일의 경로를 적어준다.
    cap = cv2.VideoCapture(0)
    baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
    detector = cv2.CascadeClassifier(baseUrl + 'haarcascade_frontalface_default.xml')
    
    while (True):
        ret, img = cap.read()
        img = cv2.imread(path,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
        cv2.imwrite(path, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()