import numpy as np
import cv2 as cv

img = cv.imread('Photos\Euro.jpg')
cv.imshow('image', img)

#simple thresholding
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscaled", gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded Image", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresholded Image Inverse", thresh_inv)

#Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255,
                 cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 18)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)