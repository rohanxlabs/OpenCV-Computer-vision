import cv2 as cv
image = cv.imread('Photos/park.jpg')

if image is  None:
    print("Image not found")

else:
    print("Image found")


#resizing
resized = cv.resize(image, (300, 300))

cv.imshow('Original Image', image)
cv.imshow('Resized Image', resized)

cv.imwrite('Photos/park_resized.jpg', resized)
cv.waitKey(0)
cv.destroyAllWindows()