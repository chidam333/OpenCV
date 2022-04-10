import cv2
import numpy as np

#----------------------------------- Not initially, do only after showing blurr image, then do this ----------------------------------------#
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



def contoursfind(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt) #finding the area of the contours
        print(area)
        if area > 500: # we keep the area greater than 500, to remove distortion, 
            cv2.drawContours(imgCopy,cnt,-1,(255,0,0),5) #-1 indicates that all the identified contour points must be drawn
            peri = cv2.arcLength(cnt,True) #calculate the perimeters
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #Epsilon is an approximation factor, that determines the accuracy of identifying the edges.
            
            #print(approx) #Show how the output array is . Explain it.
            print(len(approx)) #Gives us the number of edges for each image.
            
            edges_no = len(approx)
            
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgCopy,(x,y),(x+w,y+h),(0,233,120),2,cv2.LINE_AA) # drawing a rectangle around each shape using x,y,w,h from boudningRect
            object_type = "None"
            if edges_no == 3:
                object_type = "Tri"
                
            elif edges_no == 4:
                #To differentiate between square and rect, find the aspect ratio
                aspectRatio = w/h
                if aspectRatio >= 0.95 and aspectRatio <= 1.05: #range catering to small variations
                    object_type = "square"
                else:
                    object_type = "rect"
            
            else:
                object_type = "circle"    
            cv2.putText(imgCopy,object_type,(x + (w//2),y + (h//2)),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2) # Here we insert the text at the center. 
            #Hence the org paramters is (x + (w//2),y + (h//2)) that determines the center of each shape.
            
            
            
            
            
            
#------------------------------------------------------------------------------------------------------------#

img = cv2.imread(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\shapes.png")

#------------------------------
#Do this only after cv2.contourArea()
imgCopy = img.copy()

#------------------------------
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imgGray,(7,7),1)

#----------------------------------
height,width,channel = img.shape
#-----------------------------------
#After blurr we perform the edge detection
edgeImage = cv2.Canny(blur,50,50)
#-----------------------------------


#To fit equal number of images in the next row, we use np.zeros
black = np.zeros([width,height],np.uint8) #We can also use np.zeros_like(img)-> Basically it creates a matrix like "img" having all zeros.

#-----------------------------------
    
#Only after creating the contour function   
contoursfind(edgeImage)#calling the function  
    
    
#Not initially, only after showing the blurr images
#Initial stackedImg
#stackedImg = stackImages(0.7,[img,imgGray,blur]) #Using the stack function to stack our images.


#NextStackedImage
stackedImg = stackImages(0.6,([img,imgGray,blur],[edgeImage,imgCopy,black]))  #imgCopy not to be included initially, to be used only after cv2.drawContours





cv2.imshow("Stacked",stackedImg)

'''
#After showing this, then use the stack function 

cv2.imshow("Original",img)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("blur Image",blur)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()