
import cv2 as cv 
import numpy as np 

import matplotlib.pyplot as plt
                                                    # It allows us to visulise the pixek intensities in the image 
cat= cv.imread('photos\Cats.jpg')
cv.imshow('cat',cat)


plt.figure()
plt.title('color Histograms')
plt.xlabel('Bins')
plt.ylabel('No of histograms')



color = ('b','g','r')
for i , col in enumerate(color):
 
 hist = cv.calcHist([cat],[i],None,[256],[0,256])
 plt.plot(hist, color=col)
 plt.xlim([0,256])

plt.show()
cv.waitKey(0) 
 
 
 
 

# Histograms computing 

# gray =cv.cvtColor( cat,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)


# # Grayscale Histograms 

# Gray_histograms = cv.calcHist([gray],[0],None,[256],[0,256])

# plt.figure()
# plt.title('Grayscale Histograms')
# plt.xlabel('Bins')
# plt.ylabel('No of histograms')
# plt.plot(Gray_histograms)
# plt.xlim([0,256])
# plt.show()



# for colour images 

    







