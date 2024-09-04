


import cv2 as cv 





img = cv.imread('D:\Robotics\Programming Language\Python\OpenCv Basics\photos\sunset-photography-blog-1-Copy.webp')
cv.imshow('cat',img)

# # Convert to grayscale 

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# # BGR to HSV

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("hsv",hsv)

# # BGR to L*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
# cv.imshow('lab,',lab)

# BGR to RGB

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)



cv.waitKey(10000)
cv.destroyAllWindows()