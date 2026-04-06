import cv2 as cv

image = cv.imread('Photos/cats.jpg')

if image is not None:
    cropped = image[100:200, 50:150]
    
    cv.imshow("Original Image", image)
    cv.imshow("Cropped Image", cropped)
    cv.waitKey(0)
    cv.destroyAllWindows()
