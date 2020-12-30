import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos\Euro.jpg')
blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('image', img)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)


# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("GrayImage", gray)

masked_image = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Mask', masked_image)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title('Grayscal Histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

#Color Histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
    plt.xlabel('Bins')
    plt.ylabel('Number of pixels')
plt.show()

cv.waitKey(0)
