import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\text.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#---- DO THISS FIRST----------
 #print(pytesseract.image_to_string(img))
#------------------
#Splitlines() method basically returns a list with all the lines in a string.
#The output of image_to_boxes, is a string with dimensions of each character of a single line.
#Now we convert this into a list by using splitlines.
#Then we extract each item in the list by using a for loop.

height,width,channel = img.shape




boxes = pytesseract.image_to_boxes(img)
print(boxes)
print(boxes.splitlines())
for b in boxes.splitlines():
    #Split at each space
    b = b.split(' ') #splitting the values in each item to further access each item 
    print(b)
    # All the values in the list are strings and need to be converted to integers.
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    print(x,y,w,h)
    
    #--------------- do this first ----------------
    #Now we create the bounding boxes with x,y,w,h
    
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1,cv2.LINE_4)
        
    #But the output is not proper. The boxes overlap
    #The reason is with the points. The X-point is fine. But The Y - point is wrong.
    
    #--------------------
    
     
    #Show how the Y-point is wrong in the ouput image.
    #The Y -point is opposite (i.e. take from bottom to top but in cv2 it is take from top to bottom)
    # Show how the box is located VVVVVVVVVIP
    #So we need to subtract our image height form y. Means Imgheight - y = the other height
    #Moreover the w,h are aldready given with x,y. So no need to add them
    
    cv2.rectangle(img,(x,height - y),(w,height - h),(255,255,0),1,cv2.LINE_4)
    cv2.putText(img,b[0],(x,height-y + 20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
    
    
cv2.imshow("RGB",img)
cv2.waitKey(0)