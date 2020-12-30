import numpy as np
import cv2 as cv

img = cv.imread('Photos\Euro.jpg')
blank = np.zeros(img.shape[:2], dtype = "uint8")
cv.imshow('image', img)
cv.imshow("Blank", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("mask", mask)



masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Masked image", masked)

cv.waitKey(0)