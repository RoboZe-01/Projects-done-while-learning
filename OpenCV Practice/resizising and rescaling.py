
import  cv2 as cv 

img = cv.imread( 'D:\Robotics\Programming Language\Python\OpenCv Basics\photos\me.2.jpg')
cv.imshow('prem', img)

def rescaleFrame ( frame , scale = 0.2):
    
    width = int(frame.shape[1]*scale )
    height = int(frame.shape[0]*scale)                              #in this step we make a function to rescale our img/ video 

    dimension = ( width , height)
    
    return cv.resize(frame , dimension, interpolation= cv.INTER_AREA) 

resized_img = rescaleFrame(img)
cv.imshow('prem',resized_img)


# capture = cv.VideoCapture('D:\Robotics\Programming Language\Python\OpenCv Basics\Videos\just do it.mp4') 

# # as we want to play a video for that specific period of time we r using while loop 
# # in while we use frame variable so the viddeo get read frame by frame 

# while True :

#     isTrue , frame = capture.read() 
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('video', frame)
#     cv.imshow('video resized',frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()    