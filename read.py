import numpy as np
import cv2 as cv

# my_img = cv.imread('Photos\Euro.jpg')
# cv.imshow('image', my_img)


# cv.waitKey(0)

#Reading videos

capture = cv.VideoCapture('videos\GWR.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)



    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
