

import cv2 as cv 
sunset = cv.imread('D:\Robotics\Programming Language\Python\OpenCv Basics\photos\sunset-photography-blog-1-Copy.webp')
img = cv.imread('photos/boston.webp')
cv.imshow('img',sunset)

# SPliting the color channel 


b,g,r = cv.split(sunset)
cv.imshow('blue',b)
cv.imshow('Green',g)
cv.imshow('red',r)

print(sunset.shape)

print(b.shape)

print(g.shape)
print(r.shape)

# merging the image means all the split color merge together

merged = cv.merge([b,g,r])
cv.imshow('merge',merged)




cv.waitKey(0)