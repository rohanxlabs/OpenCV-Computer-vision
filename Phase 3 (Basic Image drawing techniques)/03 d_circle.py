import cv2 as cv

image = cv.imread('Photos/cats.jpg')

if image is None:
    print("Image not found")
else:
    print("Image found")
    thickness = 3
    center = (200, 200)
    radius = 100
    color = (0, 0, 255)
    cv.circle(image, center, radius, color, thickness)
    cv.imshow('Circle', image)
    cv.waitKey(0)
    cv.destroyAllWindows()