import cv2
import numpy as np

img = cv2.imread(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\lena.png")
 #--------------------- FIRST PART ----------------------------------------------------------------------------------------------------#
hor = np.hstack((img,img,img)) # It takes in a tuple (image1,image2). image1 and image2 are the images to be combined horizontally
ver = np.vstack((img,img))
 #--------------------- FIRST PART ----------------------------------------------------------------------------------------------------#

 #--------------------- SECOND PART ----------------------------------------------------------------------------------------------------#
 
 #Dont explain this part of code ----- JUST TELL IT IS USED TO STACK IMAGES
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: 
                    imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: 
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

stacked_img_horizontal =  stackImages(0.5,([img,img,img]))
stacked_img_vertical =  stackImages(0.5,([img,img,img],[img,img,img]))
rgb_gray_image = stackImages(0.5,([img,gray_image,img],[img,gray_image,img]))
cv2.imshow("The horizontal stack image",hor)
cv2.imshow("Vertical image",ver)
cv2.imshow("stacked_images",stacked_img_horizontal)
cv2.imshow("stacked_images_vertical",stacked_img_vertical)
cv2.imshow("BGR AND GRAY",rgb_gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()