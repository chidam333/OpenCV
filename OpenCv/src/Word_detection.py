import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(r"C:\Users\hshas\Downloads\text.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


height,width,channel = img.shape

#Show the output of each part VVVIP

boxes = pytesseract.image_to_data(img)
#Here the output has more number of columns than image_to_boxes
#A row not having any word has 11 columns
# But A row having a word has 12 columns

print(boxes)
print(boxes.splitlines())

#First show like this "for b in boxes.splitlines()"
# Then show like  for x,b in enumerate(boxes.splitlines()): We do this to remove the headings.
for x,b in enumerate(boxes.splitlines()):
    #Split at each space
    if x!= 0:
        #Here i did not use " .split(' ') ". Tell why
        b = b.split() #splitting the values in each item to further access each item 
        
        print(b)
    #Since we need only those rows with more than 12 columns
    
        if len(b) == 12:
            
            #Since we have 12 columns
            #The values for the bounding box begin from 6th position in the list. Show through the terminal.
            #
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            #print(x,y,w,h)


            #Unlike for image_to_boxes, where the height was opposite, here we use the previous convention. Tell in a funny way.

            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1,cv2.LINE_4)
            cv2.putText(img,b[11],(x,y - 8),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
        
    
cv2.imshow("RGB",img)
cv2.waitKey(0)