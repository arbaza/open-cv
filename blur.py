import numpy as np
import cv2 as cv

img = cv.imread('Photos\Euro.jpg')
cv.imshow('image', img)

#Averaging
average = cv.blur(img, (5, 5))
cv.imshow("Blur", average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow("Gaussian blur", gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

#Bilateral blur
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)