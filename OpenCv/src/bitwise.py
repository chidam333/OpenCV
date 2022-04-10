from pickletools import uint8
import cv2
import numpy as np

blank1 = np.zeros((500,500),np.uint8)
rectangle = cv2.rectangle(blank1,(50,50),(400,400),(255,255,255),cv2.FILLED)

blank2 = np.zeros((500,500),np.uint8)
circle = cv2.circle(blank2,(250,250),200,(255,255,255),cv2.FILLED)

andbit = cv2.bitwise_and(blank1,blank2)
andor = cv2.bitwise_or(blank1,blank2)
andxor =  cv2.bitwise_xor(blank1,blank2)

cv2.imshow("BLANK1",blank1)
cv2.imshow("BNLANK2",blank2)
cv2.imshow("AND",andbit)
cv2.imshow("OR",andor)
cv2.imshow("XOR",andxor)
cv2.waitKey(0)
