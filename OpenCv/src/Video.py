import cv2

cap = cv2.VideoCapture(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\Traffic.mp4")

if(cap.isOpened() == False):
    print("Video not captures")
    
while(cap.isOpened()):
    success,img = cap.read()
     #---------not initially------------#
    
    img = cv2.resize(img,(800,600),cv2.INTER_AREA) #cv2.INTER_AREA will shrink the image
    
    #---------not initially------------#
    cv2.imshow("Video",img)
   
    if cv2.waitKey(1) & 0xFF == ord('q'): # when q is pressed, checking whether q iss pressed
        break # come out of the while loop