

# Thresholding of img means representing the img in a binary format 



import cv2 as cv
import numpy as np
import matplotlib.pyplot


img = cv.imread('photos\Cats.jpg')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray ', gray)


# Simple thresholding 

threshold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)  

# what this do is when compare the threshold value in the img in this lim 150 to 255
# if the value is below the min it return 0 and if above it gives 1 or 255 colour
#  in this case if below = black and  above = white


#  thresh = binarized img
# threshold = the same value u passed is return to it 

threshold , thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)  
# cv.imshow('threshold inverse',thresh_inv)
# cv.imshow('Simple thresholded', thresh)



# Adaptive threshold

# Difference between simple and adaptive thresholding is that in adaptive thresholding the computer decide the optimum intensity on his own


adaptive_thresh = cv.adaptiveThreshold(gray , 255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive Threshold',adaptive_thresh)


cv.waitKey(0)
