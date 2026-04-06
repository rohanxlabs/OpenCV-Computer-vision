import cv2 as cv

image = cv.imread('Photos/cats.jpg')

blurred = cv.GaussianBlur(image, (7, 7), 0)

cv.imshow("Original Image", image)
cv.imshow("Blurred Image", blurred)
cv.waitKey(0)
cv.destroyAllWindows()