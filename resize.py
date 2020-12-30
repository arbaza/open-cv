import numpy as np
import cv2 as cv

# my_img = cv.imread('Photos\Euro.jpg')
# cv.imshow('image', my_img)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
    

def rescale_frame(frame, scale = 1/3):
    width = frame.shape[1] * scale
    height = frame.shape[0] * scale
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('videos\GWR.mp4')

while True:
    isTrue, frame = capture.read()
    print (frame.shape)
    frame_resized = rescale_frame(frame, scale = 0.2)

    cv.imshow('Video', frame)
    
    cv.imshow('Video', frame_resized)




    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)