

import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')            # we have created blank img here (500,500) is width and height and uint8 in data type for images
cv.imshow('Blank',blank)                            
img = cv.imread('D:\Robotics\Programming Language\Python\OpenCv Basics\photos\me.2.jpg')

# colouring the image 

blank[:]=(200,255,255)      # opem cv follows BGR system (blue , green , red )
cv.imshow('blue',blank)
cv.waitKey(0)

# Draw rectangle 

cv.rectangle(blank,(0,0),(250,250),(250,50,200),  thickness = 2)  # this rectagle is not filled with colour
cv.rectangle(blank,(0,0),(500,200),(250,50,200),  thickness = -1)  # this rectagle is filled with colour
cv.imshow('rectangle ', blank)

# Draw a circle 

cv.circle(blank, (250,250),(50),(250,250,250), thickness = -4)
cv.imshow('circle', blank)

# Draw Line 
cv.line(blank , (0,0),(250,250),(255,0,0),  thickness =5)
cv.imshow('line',blank )

# Write text on the image 

cv.putText(blank,'Hii , how are you ',(2,250),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),1,)
cv.imshow('text', blank)



cv.waitKey(10000)
cv.destroyAllWindows