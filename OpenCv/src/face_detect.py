import cv2

#Loading the haar cascade classifier file
facecascade = cv2.CascadeClassifier(r"E:\python 310\codePRAC\OpenCv\resources\haarcascades\haarcascade_frontalface_default.xml")
img = cv2.imread(r"E:\python 310\codePRAC\OpenCv\resources\lena.png")

imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Using the loaded cascade, we find the faces in our GRAY image. The 2nd paramter is the scale and the third parameter is the minimum number of neighbours.
# the output faces, consists of the widht, height and x and y coordinates.
faces = facecascade.detectMultiScale(imgGRAY,1.1,4)
print(faces) # Show the output
#The we create a bounding box around the face by using the widht, height and x and y values

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(120,10,10),3,cv2.LINE_AA)
    
cv2.imshow("Original",img)
cv2.imshow("Gray",imgGRAY)

cv2.waitKey(0)
cv2.destroyAllWindows()

