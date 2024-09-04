


import cv2 as cv
import numpy as np

people = cv.imread('D:\Robotics\Programming Language\Python\OpenCv Basics\photos\me.2.jpg')

cv.imshow('people',people)

gray = cv.cvtColor(people, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('haar cascade faceDetection.xml')

face_rect = haar_cascade.detectMultiScale(gray , scaleFactor=1.1,minNeighbors=3)

print(f'Number of faces foun = {len(face_rect)}')

cv.waitKey(0)