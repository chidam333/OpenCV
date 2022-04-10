
import cv2
import numpy as np
kernel=np.ones((3,3),np.uint8)
print(kernel)
image1=cv2.imread(r"E:\python 310\codePRAC\OpenCv\resources\lena.png")
# image1=cv2.imread(r"E:\python 310\codePRAC\OpenCv\resources\lambor.jpg")
gray=cv2.cvtColor(image1,cv2.COLOR_RGB2GRAY)
blur=cv2.GaussianBlur(gray,(7,7),5)
edge=cv2.Canny(blur,100,100)
dilate=cv2.dilate(edge,kernel,iterations=2)
eroded=cv2.erode(edge,kernel,iterations=1)
cv2.imshow("blur",blur)
cv2.imshow("dilate",dilate)
cv2.imshow("erode",eroded)
cv2.imshow("edge",edge)
cv2.imshow("gray image",gray)
cv2.imshow("image",image1)
cv2.waitKey(20000)