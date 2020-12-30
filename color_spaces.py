import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos\Euro.jpg')
cv.imshow('Image', img)

# plt.imshow(img)
# plt.show()

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#HSV Hue saturation value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

#HSV to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_bgr)

plt.imshow(rgb)
plt.show()


cv.waitKey(0)