import numpy as np
import cv2 as cv

img = cv.imread('Photos\Euro.jpg')
cv.imshow('image', img)
cv.waitKey(0)

#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

#Edge cascade
edge = cv.Canny(img, 125, 175)

#dilate
dilate = cv.dilate(edge, (3, 3), iterations = 1)

#eroding
eroded = cv.erode(dilate, (3,3), iterations = 1)

#resize
resize = cv.resize(img, (200, 200), interpolation = cv.INTER_CUBIC)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
