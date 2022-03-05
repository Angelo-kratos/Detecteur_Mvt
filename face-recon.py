#importation des modules
import numpy as np
import cv2 as cv
import face_recognition


image = face_recognition.load_image_file("/home/kratos/Documents/opencv/photos/waren2.jpg") #load file
face_loc = face_recognition.face_locations(image)[0] #trouver la partie du visage
face_encoded = face_recognition.face_encodings(image)[0] #encoder le visage 128 measurment
cv.rectangle(image,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(0,255,0),2)
imgRgb = cv.cvtColor(image,cv.COLOR_BGR2RGB,None,None)


image1 = face_recognition.load_image_file("/home/kratos/Documents/opencv/photos/waren1.jpg") #load file
face_loc1 = face_recognition.face_locations(image1)[0] #trouver la partie du visage ==+ liste-tuple
face_encoded1 = face_recognition.face_encodings(image1)[0] #encoder le visage ==+list-tuple
cv.rectangle(image1,(face_loc1[3],face_loc1[0]),(face_loc1[1],face_loc1[2]),(0,255,0),2)
imgRgb1 = cv.cvtColor(image1,cv.COLOR_BGR2RGB,None,None)

#Afficher les deux images avec les 02 rectangle qui detecte les parties du visage
cv.imshow("face_located",imgRgb)
cv.imshow("face_located1",imgRgb1)

result = face_recognition.compare_faces([face_encoded],face_encoded1, )    #comparer les deux face
faceDist = face_recognition.face_distance([face_encoded],face_encoded1) #rassemblence
print(result,faceDist)
cv.waitKey(0)