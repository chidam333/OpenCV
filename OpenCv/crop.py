import cv2
img=cv2.imread(r"E:\python 310\codePRAC\OpenCv\resources\lena.png")
resize=cv2.resize(img,(300,500))
imgCrop=img[0:200,0:200]
cv2.imshow("cropimg",imgCrop)
cv2.imshow("resize",resize)
cv2.waitKey(0)
