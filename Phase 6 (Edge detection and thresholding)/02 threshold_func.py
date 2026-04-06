import cv2 as cv

img = cv.imread('Photos/cats.jpg', cv.IMREAD_GRAYSCALE)

ret, thresh_img = cv.threshold(img, 150, 255, cv.THRESH_BINARY)

cv.imshow('Original', img)
cv.imshow('Thresholded', thresh_img)
cv.waitKey(0)
cv.destroyAllWindows()