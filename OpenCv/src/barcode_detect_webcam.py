import cv2
import numpy as np
from pyzbar.pyzbar import decode


cam = cv2.VideoCapture(0)

while(cam.isOpened()):
    success,frame = cam.read()
    for barcode in decode(frame):
        print(barcode.data)
        mydata = barcode.data.decode('utf-8')
        print(mydata)
        #Forming a boudning box
        points = np.array([barcode.polygon],np.int32)
        print(points)
        
        points = points.reshape((-1,1,2)) # -1 is an unspecified value that is inferred.
        cv2.polylines(frame,[points],True,(255,0,123),5)
        point = barcode.polygon
        print(point[0])
        cv2.putText(frame,mydata,point[0],cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),4)
        
        #Also try putting the text using the rectangle points.
        
        
        
    cv2.imshow("Result",frame)
    cv2.waitKey(1)
