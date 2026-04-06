import cv2 as cv 

img = cv.imread('Photos/cats.jpg', cv.IMREAD_GRAYSCALE)

edges = cv.Canny(img, 100, 200)

cv.imshow('Original', img)
cv.imshow('Edges', edges)
cv.waitKey(0)
cv.destroyAllWindows()
