import numpy as np
import cv2 as cv

img = cv.imread('Photos\Euro.jpg')
cv.imshow('image', img)

#Laplacian
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grauscaled", gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) 
combinedsobel = cv.bitwise_or(sobelx, sobely)


cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel XY', combinedsobel)

cv.waitKey(0)