import numpy as np
import cv2 as cv

img = cv.imread('Photos\Euro.jpg')
cv.imshow('image', img)
cv.waitKey(0)

#translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, -100)

#rotation
def rotate(img, angle, rotpoint = None):
    (height, width) = img.shape[:2]
    if rotpoint is None:
        rotpoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, 45) 

#Resizing
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)

#flip
flip = cv.flip(img, -1)



cv.imshow("Flipped", flip)


cv.waitKey(0)