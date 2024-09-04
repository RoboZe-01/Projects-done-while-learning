

import cv2 as cv 
import numpy as np 


cat = cv.imread('photos\Cats.jpg')
cv.imshow('cat',cat)


gray = cv.cvtColor(cat,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#  laplance method

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

cv.waitKey(10000)