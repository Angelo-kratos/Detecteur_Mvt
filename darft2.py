import cv2 as cv

img1 = cv.imread("/home/kratos/Documents/opencv/photos/post1.jpg")
img2 = cv.imread("home/kratos/Documents/opencv/photos/post2.jpg")

#diff = cv.absdiff(img1,img2)
cv.imshow("diff",img1)
cv.waitKey(0)