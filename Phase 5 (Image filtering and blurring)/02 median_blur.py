import cv2 as cv

image = cv.imread('Photos/cats.jpg')

blurred = cv.medianBlur(image, 5)

cv.imshow('Original', image)
cv.imshow('Blurred', blurred)
cv.waitKey(0)
cv.destroyAllWindows()
