import cv2
import numpy as np



    
#Created an array for three color Blue,Green,Red. Get from colorpicker.py show juniors how to do.
color = [[95,84,79,118,217,255],[39,42,106,82,255,255],[10,98,29,40,255,249]]  #(in the form of (Hmin,Smin,Vmin,Hmax,Smax,Vmax))



#-----------Do this after opening the camera and also after finding the color HSV values
#Color detection code
def findColor(img,color):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    #lower = np.array([h_min,s_min,v_min]) h_min,s_min,v_min will be taken from the color array
    #upper = np.array([h_max,s_max,v_max])
    for col in color:
        lower = np.array(col[0:3]) #In 0th position takes the elements 0 , 1 , 2
        upper = np.array(col[3:6])
    
        mask = cv2.inRange(imgHSV,lower,upper)
        cv2.imshow(str(col[0]),mask)#We cannot use the same window name, because we have three different colors.
        
    
#---------------------- Video.py code -------------------------#
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,130)
while(cam.isOpened()):
    success,frame = cam.read()
    cv2.imshow("Camera",frame)
    findColor(frame,color)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#---------------------- Video.py code ----------------------------#
