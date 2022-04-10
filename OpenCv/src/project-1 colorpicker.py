import cv2
import numpy as np


def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,300)

cv2.createTrackbar("Hue min","TrackBars",0,179,empty) 
cv2.createTrackbar("Hue max","TrackBars",179,179,empty)   
cv2.createTrackbar("Sat min","TrackBars",0,255,empty) 
cv2.createTrackbar("Sat max","TrackBars",255,255,empty) 
cv2.createTrackbar("Value min","TrackBars",0,255,empty) 
cv2.createTrackbar("Value max","TrackBars",255,255,empty) 

#Getting the value for the tracker bars

while True:
    cam = cv2.VideoCapture(0)
    while(cam.isOpened()):
        success,img = cam.read()
        imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        
        #Creating trackbars

        #We need to create 6 Trackbars Hue min/max, Sat min/max, Value min/max
        
        h_min = cv2.getTrackbarPos("Hue min","TrackBars")
        h_max = cv2.getTrackbarPos("Hue max","TrackBars")
        s_min = cv2.getTrackbarPos("Sat min","TrackBars")
        s_max = cv2.getTrackbarPos("Sat max","TrackBars")
        v_min = cv2.getTrackbarPos("Value min","TrackBars")
        v_max = cv2.getTrackbarPos("Value max","TrackBars")
        
        print(h_min,h_max,s_min,s_max,v_min,v_max)
        
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])
        
        mask = cv2.inRange(imgHSV,lower,upper) #Creates the threshold for a give color range.
        
        #In Workshop explain why we put in while, because we need to extract the values from the trackbar continuously. Thus we provide infinite iterations.
        #Explain diagramatically, how it occur on the board
        


        img = cv2.resize(img,(700,500))
        imgHSV = cv2.resize(imgHSV,(700,500))
        
        mask = cv2.resize(mask,(700,500)) #At this point vary the taskbar points to get the body of the car. Ask the juniors to do this. The color we want to get must be white.
        imgResult = cv2.bitwise_and(img,img,mask = mask) # Apply the mask over the original image using bitwise_and and show the output.


        cv2.imshow("BGR_IMAGE",img)
        cv2.imshow("HSV_Image",imgHSV)
        cv2.imshow("Mask",mask)
        cv2.imshow("Image",imgResult)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break


    ''' 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''