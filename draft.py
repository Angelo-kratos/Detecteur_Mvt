import cv2 as cv
from cv2 import absdiff
from cv2 import boundingRect
import numpy as np

webcam = cv.VideoCapture("videos/vidTest.avi")
ret, imageframe1 = webcam.read() # get frame per frame from the webcam
ret, imageframe2 = webcam.read() 
if webcam.isOpened():
    while True:
        diff = absdiff(imageframe1,imageframe2)
        gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray,(5,5),0)
        _,thresh = cv.threshold(blur,20,255,cv.THRESH_BINARY)
        dilate = cv.dilate(thresh,None,3)
        contours,_ =cv.findContours(dilate,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            (x,y,w,h)=boundingRect(contour)

            if cv.contourArea(contour)<700:
                continue
            cv.rectangle(imageframe1,(x,y),(x+w,y+h),(0,255,0),2)
        #cv.drawContours(imageframe1,contours,-1,(0,255,0),2)
        if ret:
            cv.imshow('CApVideos', imageframe1) # show the frame
            imageframe1 = imageframe2
            ret,imageframe2 = webcam.read()
        else:
            print('No image available')
        keystroke = cv.waitKey(20) # Wait for Key press
        if (keystroke == 27):
            break # if key pressed is ESC then escape the loop
 
    webcam.release()
    cv.destroyAllWindows()  