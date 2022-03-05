import cv2 as cv
import mediapipe as mp
import numpy as np
import time

face_cascade = cv.CascadeClassifier("/home/kratos/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt.xml")

utils = mp.solutions.drawing_utils
face_mesh = mp.solutions.face_mesh
faceMesh = face_mesh.FaceMesh(max_num_faces=1)
feature_draw = utils.DrawingSpec(color=(0,255,0),thickness=1,circle_radius=2)

cap = cv.VideoCapture(0)
captured = cap.isOpened()

def countdown(t):
    for t in range(5,0,-1):
        print(t)
        time.sleep(1)
    print("demarer")
countdown(5)

if captured:
    while True:
        _,frame = cap.read()
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
            cv.imshow("frame", frame)
            image_croped = frame[y:y+h , x:x+w]
            keystore = cv.waitKey(20)

            if (keystore == 27):
                cv.destroyWindow("frame")
                imgRgb = cv.cvtColor(image_croped,cv.COLOR_BGR2RGB)
                results = faceMesh.process(imgRgb)
                if results.multi_face_landmarks:
                    for faceLms in results.multi_face_landmarks:
                        utils.draw_landmarks(image_croped,faceLms,face_mesh.FACEMESH_CONTOURS,feature_draw,feature_draw)
                        cv.imshow("image_croped", image_croped)
            elif (keystore == ord('q')):
                break

    cap.release()
    cv.destroyAllWindows()

