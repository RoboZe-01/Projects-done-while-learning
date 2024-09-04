
import cv2 as cv 
import numpy as np


img = cv.imread('photos\Cats.jpg')
cv.imshow('cats',img)

# we r gonna learn the methods to blur the images 
# the first one is basic guassian blur 


# blur = cv.GaussianBlur(img, (5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# second method is Averaging method 

average = cv.blur(img ,(3,3))

cv.imshow("avg blur ",average)

# Median blur 

median = cv.medianBlur(img,3)
cv.imshow('median',median)


cv.waitKey(10000)
cv.destroyAllWindows()