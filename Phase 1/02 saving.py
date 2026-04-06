import cv2 as cv

image = cv.imread('Photos/cats.jpg')

if image is not None:
    success = cv.imwrite('Photos/cat_copy.jpg', image)
    if success:
        print("Image saved successfully.")
    else:
        print("Failed to save the image.")