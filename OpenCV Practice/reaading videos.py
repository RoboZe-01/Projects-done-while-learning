
import cv2 as cv 

 # define the path we want the video from 

capture = cv.VideoCapture('D:\Robotics\Programming Language\Python\OpenCv Basics\Videos\just do it.mp4') 

# as we want to play a video for that specific period of time we r using while loop 
# in while we use frame variable so the viddeo get read frame by frame 

while True :

    isTrue , frame = capture.read() 
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()    





