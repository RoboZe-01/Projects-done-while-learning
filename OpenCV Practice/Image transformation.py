import cv2 as cv 
import numpy as np

img = cv.imread('D:\Robotics\Programming Language\Python\OpenCv Basics\photos\me.2.jpg')

cv.imshow ('Me',img )

def Translate (img,x,y):

    transMat = np.float32([[1,0,x],[0,1,y]])       # this is used to translate the image 
    dimension = (img.shape[1],img.shape[0])        # 1 = width , 0 = height
    return cv.warpAffine(img,transMat,dimension)

# x= -ve shift towards left 
# y = -ve shift towards down
translated=Translate(img,100,100)
cv.imshow('Translated',translated)

# Rotation of the image 

def rotate (img,angle ,rotpoint=None ):
    (height,width)= img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2,height//2)

    rotMat =cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions = (width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)

cv.imshow('rotated',rotated)




# Image resized 

resize = cv.resize(img,(750,750), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resize)

# Flipping the image 

flip = cv.flip(resize,0)
cv.imshow('flip',flip)



cv.waitKey(20000)
cv.destroyAllWindows()

