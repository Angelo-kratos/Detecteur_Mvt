import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
x=2
photo =cv.imread("/home/kratos/Documents/opencv/photos/test1.jpeg")
cv.imshow("photo",photo)

tbl_photo = np.array(photo)
col_plat = tbl_photo[:,:1,(1)].flatten()
col_plat1 = tbl_photo[:,:1,(2)].flatten()
plt.hist(col_plat,bins=255)
plt.hist(col_plat1,bins=255)
#print(col_plat1)
plt.show()

blank_vide = np.zeros((300,300,3),dtype=np.uint8)
blank_vide[:]=120,23,90
cv.imshow("photo1",blank_vide)
cv.waitKey(0)

plt.hist2d(col_plat,col_plat1)
plt.colorbar()
plt.show()
exp = np.linspace(0,20,400)



enter_text=str(input("Entrer votre nom: "))

cv.putText(blank_vide,enter_text,(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("photos",blank_vide)


