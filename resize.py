import cv2 as cv
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale) #shape[1] is horizontal
    height=int(frame.shape[0] * scale)#shape[0] is vertical
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


#image resize
img=cv.imread('D:\Projects\opencv-course\Resources\Photos\cat_large.jpg')
resized_img=rescaleFrame(img,scale=0.1)
cv.imshow("image",resized_img)#resized img
cv.imshow("original",img)#original
cv.waitKey(0)


#reading video
capture=cv.VideoCapture('D:\Projects\opencv-course\Resources\Videos\dog.mp4')#0 means first cam, we can also specify the file path here
while True:
    isTrue,frame=capture.read()#reads video frame by frame

    #new frame
    frame_resized=rescaleFrame(frame,scale=0.1)#calling out func and changing scale
    cv.imshow('Video',frame)#diplay original
    cv.imshow("video resized",frame_resized)#resized

    if cv.waitKey(20) & 0xFF==ord('d'):
        break #if d is pressed then stop video
capture.release()
cv.waitKey(0)



