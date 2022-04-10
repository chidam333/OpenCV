import cv2
cam = cv2.VideoCapture(0)
while(cam.isOpened()):
    success,frame=cam.read()
    cv2.imshow("cam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break