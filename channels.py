import numpy as np
import cv2 as cv

img = cv.imread('Photos\Euro.jpg')
blank = np.zeros(img.shape[:2], dtype = 'uint8')

cv.imshow('image', img)


b, g, r = cv.split(img)
blue = cv.merge([b, blank, blank])
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

cv.imshow('Blue_b', blue)
cv.imshow('Green_g', green)
cv.imshow('Red_r', red)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)