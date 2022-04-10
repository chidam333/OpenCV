import cv2
import numpy as np

#--------------------------- PART 1 -----------------------------------------------------------------------------#
img1 = np.zeros((512,512),np.uint8) # Creating a black image consisting of 512 * 512 pixels. This is a Binary image
print(img1.shape)
img2 = np.zeros((512,512,3),np.uint8) #Adding 3 channels to the image. This image includes pixels values from 0 to 254. 
print(img2.shape)

#img2[:] = 255,0,0 # Allow the juniors to take over a range of values. Also try by removing the channel from dsize.
#---------------------------- END OF PART 1 -----------------------------------------------------------------------#


#------------------- PART 2 ---------------------------------------------------------------------------------------#
#Adding a line to an image

#This first 
#cv2.line(img2,(0,0),(300,300),(240,120,120),3) # To get color on an image, the image must have 3 channels


#Second -> Drawing a full line by sing height and width. 
height = img2.shape[0] # Shape gives an array of [height,width,channels]. This gives the height
width = img2.shape[1] # This gives the width
channels = img2.shape[2] # This gives the number of channels
cv2.line(img2,(0,0),(width,height),(255,120,34),3)  # The dsize or points are always (width,height). Only slicing is different.



#Third drawing a rectangle
cv2.rectangle(img2,(0,0),(400,400),(0,0,255),4)
#To get a filled rectangle we use a constant
#cv2.rectangle(img2,(0,0),(400,400),(0,255,255),cv2.FILLED)

#Drawing a circle.
cv2.circle(img2,(400,400),30,(255,255,0),cv2.FILLED) # Also show how this can be filled. Filling should be done on thickness parameter


#-------------------------------- END OF PART 2 ----------------------------------------------------------------------#

#-------------------------------- PART 3 -----------------------------------------------------------------------------#

cv2.putText(img2,"HELLO WORLD!!",(100,100),cv2.FONT_HERSHEY_COMPLEX,4,(0,255,123),2)

#---------------------------- END OF PART 3 ---------------------------------------------------------------------------#


cv2.imshow("Blackimg",img1)
cv2.imshow("8 bit image",img2)


cv2.waitKey(0)

cv2.destroyAllWindows()
