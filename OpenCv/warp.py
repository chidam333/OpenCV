import cv2
import numpy as np
width,height = 250,350
img=cv2.imread(r"E:\python 310\codePRAC\OpenCv\resources\cards.jpg")
points1 =np.float32([[781,481],[980,359],[965,765],[1162,639]])
points2 =np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(points1,points2)
output_image = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("img",output_image)
cv2.waitKey(0)