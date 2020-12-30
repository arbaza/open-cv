import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
# blank[100:200, 300:400] = 255, 0, 0

#Rectangle
cv.rectangle(blank, (0,0), (250, 250), (0, 0, 255), thickness = cv.FILLED)

#Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness = -1 )

#line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness = 3)

#Write text
cv.putText(blank, 'Hello', (300, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (122, 127, 98), 2)
cv.imshow('Blank', blank)

# img = cv.imread('Photos\Euro.jpg')

# cv.imshow('Euro', img)
cv.waitKey(0)
