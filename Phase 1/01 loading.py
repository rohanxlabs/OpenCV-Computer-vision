import cv2 as cv

image = cv.imread('Photos/cat.jpg')

if image is not None:
    cv.imshow('Cat', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Error: Could not read the image.")