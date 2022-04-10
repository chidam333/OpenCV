import cv2
import numpy as np



width,height = 250,350 # From the image using ditance formula,take any length
img = cv2.imread(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\cards.jpg")
points1 = np.float32([[785,490],[980,360],[967,763],[1163,634]])# The card has four points.This is a multi-dimensional array having 4 rows and 2 columns
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(points1,points2) #Here we get the transformation matrix taht is applied to the original image
output_image = cv2.warpPerspective(img,matrix,(width,height)) #Fitting the transformation


cv2.imshow("Original-Image",img)
cv2.imshow("Warped-Image",output_image)

cv2.waitKey(0)

cv2.destroyAllWindows()


