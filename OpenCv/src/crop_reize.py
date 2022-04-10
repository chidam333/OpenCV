import cv2

img = cv2.imread(r"C:\Users\hshas\OneDrive\Documents\Opencv-Work\working\Scripts\resources\lambor.jpg")

print(img.shape) # Gives an output in the form of (height,width,numberofchannels)

height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

imgResize = cv2.resize(img,(300,500))
#Let us check the shape of the resized image
print(imgResize.shape)

#Allow juniors to try different values of image resizing.


#Image cropping

imgCrop = img[0:500,0:500] #height, width

cv2.imshow("Original",img)
cv2.imshow("Resized",imgResize)
cv2.imshow("CroppedImage",imgCrop)

cv2.waitKey(0)
