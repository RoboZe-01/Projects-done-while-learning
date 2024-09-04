

import cv2 as cv 
import numpy as np

img = cv.imread('D:\Robotics\Programming Language\Python\OpenCv Basics\photos\me.2.jpg')
# cv.imshow('me', img)

# Converting image into grey 

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('grey',grey)

# Blurring an image 

blur = cv.GaussianBlur(img,(5,1),cv.BORDER_DEFAULT)
# cv.imshow('bur',blur)

# Edge casade 

canny = cv.Canny(img,150,175)     # outline the edges around the object 
cv.imshow('edge',canny)            # we can reduce the noise by blurring the image which will only outline the outline of the edges 




# Dilating the image 

dilated = cv.dilate(canny , (5,5), iterations=3)   # this will imcrease the boldness of the images edges 
cv.imshow('Dilated', dilated)

# Eroding the image 

eroded = cv.erode(dilated,(5,5), iterations=3)    # this is used t0 reverse the effect of the dilating function 
cv.imshow('Eroded',eroded )


# resizing the image 

resized = cv.resize(img , (500,500))
cv.imshow( 'reszied',resized)


# cropping the image 

cropped = img[250:500,500:750]
cv.imshow('cropped ',cropped )


cv.waitKey(10000)
cv.destroyAllWindows()