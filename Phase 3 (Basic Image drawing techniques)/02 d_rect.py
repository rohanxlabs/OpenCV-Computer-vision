import cv2 as cv

image = cv.imread('Photos/cats.jpg')

if image is None:
    print("Image not found")
else:
    print("Image found")

    pt1 = (50, 100)
    pt2 = (300, 300)
    color = (0, 255, 0)  # Green in BGR
    thickness = 3

    cv.rectangle(image, pt1, pt2, color, thickness)

    cv.imshow('Rectangle', image)
    cv.waitKey(0)
    cv.destroyAllWindows() 