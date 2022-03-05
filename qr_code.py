from pyzbar.pyzbar import decode
import cv2 as cv
import numpy as np

image = cv.imread("/home/kratos/Documents/opencv/photos/images.jpeg")

code = decode(image)
for barcode in decode(image):
    pts = np.array([barcode.polygon],np.int32)
    pts =pts.reshape(-1,1,2)
    cv.polylines(image,[pts],True,(0,255,0),3)
    pts2 = barcode.rect
    cv.putText(image,str(barcode.data.decode('utf-8')),(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv.imshow("code",image)
    print(pts.shape)

cv.waitKey(0)