import cv2 as cv
import numpy as np
import mediapipe as mp


face_cascade = cv.CascadeClassifier("/home/kratos/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt.xml")
eye_cascade=cv.CascadeClassifier("/home/kratos/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/cv2/data/haarcascade_eye_tree_eyeglasses.xml")

cap = cv.VideoCapture("/home/kratos/Documents/opencv/videos/3.mp4")
marche=cap.isOpened()
if marche:

    while True:
        _,frame=cap.read()
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

        for x,y,w,h in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            graydetect=gray[y:y+h,x:x+w]
            bgrdetect=frame[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(graydetect)

            for (ex,ey,ew,eh) in eyes:
                cv.rectangle(bgrdetect,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


        cv.imshow("videos",frame)
        keystore = cv.waitKey(20)
        if keystore==(27):
            break

cap.release()
cv.destroyAllWindows()