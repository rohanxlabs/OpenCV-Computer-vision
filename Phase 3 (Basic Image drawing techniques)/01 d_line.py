import cv2 as cv 

image = cv.imread('Photos/cats.jpg')

if image is None:
    print("Image not found")

else:
    print("Image found")

    pt1 = (50, 100)
    pt2 = (300, 100)
    color = (255, 0, 0) # Blue in BGR
    thickness = 5

    cv.line(image, pt1, pt2, color, thickness)

    cv.imshow('Line', image)
    cv.waitKey(0)
    cv.destroyAllWindows()