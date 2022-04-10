import cv2
import numpy as np


# ----------------- To do this only after Canny -----------------------# 


kernel = np.ones((5,5),np.uint8)  # creating a matrix of all ones , and the values in the matrix are integers of 8 bit - u means unsigned.

#----------------- To do this only after Canny ------------------------#

imgs = cv2.imread(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\lena.png") #img is an object or an image object
imgGray = cv2.cvtColor(imgs,cv2.COLOR_BGR2GRAY) 
imgBlur = cv2.GaussianBlur(imgGray,(3,3),0) #Blurring the image
imgEdge = cv2.Canny(imgBlur,100,100)#Edgde detection, chnage the values and see
imgDilate = cv2.dilate(imgEdge,kernel,iterations= 1)  #During workshop change the values of iteration number
imgErode = cv2.erode(imgDilate,kernel,iterations=1) 


cv2.imshow("Original image",imgs)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Color Image",imgs)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("EdgeImage",imgEdge)
cv2.imshow("DilateImage",imgDilate)
cv2.imshow("Eroded Image",imgErode)
cv2.waitKey(0)