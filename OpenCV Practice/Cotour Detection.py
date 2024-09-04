

import cv2 as cv 
import numpy as np

img = cv.imread('D:\Robotics\Programming Language\Python\OpenCv Basics\photos\Cats.jpg')
cv.imshow('cat ',img)




gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray )
blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(blur,150,175)
cv.imshow('canny',canny)

Contour , hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(Contour)} found !!')



















cv.waitKey(10000)
cv.destroyAllWindows()