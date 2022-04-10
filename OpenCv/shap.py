import cv2
import numpy as np
black= np.zeros((512,512,3),np.uint8)
# print(black)
print(black.shape)
height =black.shape[0]
width =black.shape[1]
cv2.line(black,(0,0),(512,512),(0,0,255),20)
cv2.line(black,(0,512),(512,0),(0,0,255),20)
cv2.circle(black,(250,250),69,(90,255,90),cv2.FILLED)
cv2.putText(black,"OPENCV",(100,100),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,90))
cv2.rectangle(black,(200,250),(250,200),(255,0,0),20,cv2.FILLED)
cv2.imshow("black",black)
cv2.waitKey(10000)
