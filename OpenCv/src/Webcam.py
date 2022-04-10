import cv2

cam = cv2.VideoCapture(0)
cam.set(3,640) # 3 is width property and 640 is the width
cam.set(4,480) # height, 4 is the id.
cam.set(10,1) # brightness is id 10
while(cam.isOpened()):
    success,frame = cam.read()
    cv2.imshow("MyImage",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    