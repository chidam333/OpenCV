import cv2
from pyzbar.pyzbar import decode
import numpy as np

img = cv2.imread(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\barcode.png")
code = decode(img)
#-----------------------------------
print(code)
#-----------------------------------

#Explain the difference between the Rect points and polygon points

#for loop for more than one barcode

for barcode in decode(img):
    print(barcode.data)
    mydata = barcode.data.decode('utf-8')
    print(mydata)
    