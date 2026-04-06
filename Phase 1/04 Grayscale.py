import cv2 as cv

image = cv.imread('Photos/park.jpg')

if image is not None:
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('Grayscale Image', gray)
    cv.waitKey(0)
    cv.destroyAllWindows()  
else:
    print("Image not found")