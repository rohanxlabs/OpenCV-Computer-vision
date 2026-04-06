import cv2 as cv
image = cv.imread('Photos/cats.jpg')

if image is None:
    print("Image not found")
else:
    flipped_horizontal = cv.flip(image, 1)
    flipped_vertical = cv.flip(image, 0)
    flipped_both = cv.flip(image, -1)

    cv.imshow('Original', image)
    cv.imshow('Flipped Horizontal', flipped_horizontal)
    cv.imshow('Flipped Vertical', flipped_vertical)
    cv.imshow('Flipped Both', flipped_both)

    cv.waitKey(0)
    cv.destroyAllWindows()