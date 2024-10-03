import cv2 as cv
# #reading images
img=cv.imread('image.png')
cv.imshow('girls',img)
cv.waitKey(0)

#reading video
capture=cv.VideoCapture(0)#0 means first cam, we can also specify the file path here
while True:
    isTrue,frame=capture.read()#reads video frame by frame
    cv.imshow('Video',frame)#diplay each frame

    if cv.waitKey(20) & 0xFF==ord('d'):
        break #if d is pressed then stop video
capture.release()
cv.waitKey(0)