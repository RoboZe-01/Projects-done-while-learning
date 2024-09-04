
import cv2 as cv
import numpy as np


blank = np.zeros((400,400), dtype='uint8')

cv.imshow('blank',blank)

rectangle = cv.rectangle((blank.copy()),(30,30),(300,300),(255,155,100),-1)
circle = cv.circle(blank.copy(),(200,200),200,(255,155,100),-1)

# cv.imshow('rectangle ',rectangle)
# cv.imshow('circle',circle)

#Bit Wise AND

Bitwise_and = cv.bitwise_and(rectangle,circle)

cv.imshow('bitwise and',Bitwise_and)


# Bitwise Or 

Bitwise_Or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise or',Bitwise_Or)

#BitWise not 

bitwise_not = cv.bitwise_not(rectangle,circle)
cv.imshow('bitWise not',bitwise_not)

# bitwise xor 

bitwise_xor = cv.bitwise_xor(circle,rectangle)
cv.imshow('XOR', bitwise_xor)


cv.waitKey(10000)
cv.destroyAllWindows()