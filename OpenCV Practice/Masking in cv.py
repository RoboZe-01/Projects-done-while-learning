
import cv2 as cv 
import numpy as np


cat = cv.imread('photos\Cats.jpg')
blank = np.zeros(cat.shape[:2], dtype = 'uint8')

cv.imshow('blank',blank)

masking = cv.circle(blank , (cat.shape[1]//2-60, cat.shape[0]//2),100,255,-1 )

cv.imshow('mask', masking)


masked = cv.bitwise_and(cat,cat, mask= masking)
cv.imshow('masked img',masked)






cv.waitKey(0)