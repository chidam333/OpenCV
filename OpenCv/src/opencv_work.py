import cv2

cam = cv2.VideoCapture(0)

facecascade = cv2.CascadeClassifier(r"E:\python 310\codePRAC\OpenCv\resources\haarcascades\haarcascade_frontalface_default.xml")

while cam.isOpened():
    succes,frame = cam.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = facecascade.detectMultiScale(gray_frame,1.1,4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        
    cv2.imshow("Frames",frame)
    cv2.waitKey(1)
                                    