from calendar import different_locale
from pickle import NONE
import cv2 as cv
from cv2 import dilate


vid = cv.VideoCapture("videos/vidTest.avi")
ret,frame =vid.read()
ret,frame1 =vid.read()
vrai = vid.isOpened()
if vrai == False:
    print("No video found!!")
if vrai:
    while True:
        if ret==True:
            diff = cv.absdiff(frame,frame1)
            gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
            blur = cv.GaussianBlur(gray,(5,5),0)
            _,thres=cv.threshold(blur,20,255,cv.THRESH_BINARY)
            dilated =cv.dilate(thres,None,3) 
            contours,_ =cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

            for cont in contours:
                (x,y,w,h)=cv.boundingRect(cont)
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            
            #cv.drawContours(frame,contours,-1,(0,255,0),2)
            cv.imshow("videos",diff)
            frame=frame1
            ret,frame1=vid.read()

            keystore = cv.waitKey(20)
            if keystore ==  27:
                break
        else:
            break

    