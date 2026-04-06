import cv2 as cv 
import numpy as np

image = cv.imread('Photos/cats.jpg')

sharpen_kernal = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv.filter2D(image, -1, sharpen_kernal)

cv.imshow('Original', image)
cv.imshow('Sharpened', sharpened)
cv.waitKey(0)
cv.destroyAllWindows()