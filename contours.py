import numpy as np
import cv2 as cv

img = cv.imread('Photos\Euro.jpg')
cv.imshow('image', img)
cv.waitKey(0)
#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank', blank)

#blur 
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur )
# cv.waitKey(0)

#Canny/edge detection
canny = cv.Canny(img, 127, 175)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)


#Contour detection
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255 ), 1)
cv.imshow('Contours drawn', blank)
cv.waitKey(0)




# cv.imshow("Thresholded", thresh )
cv.waitKey(0)