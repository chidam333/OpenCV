#HOW TO READ IMAGES VIDEOS AND WEBCAME
import cv2 #import the package

img = cv2.imread(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\lena.png") #function to read an image. 
cv2.imshow("Output",img) #Displaying the image
cv2.waitKey(0)
