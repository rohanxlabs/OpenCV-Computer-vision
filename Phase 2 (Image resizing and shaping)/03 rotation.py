import cv2 as cv
image = cv.imread('Photos/cats.jpg')

if image is None:
    print("Image not found")
else:
    (h,w) = image.shape[:2]
    center = (w//2, h//2)
    M = cv.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv.warpAffine(image, M, (w, h))

    cv.imshow("Original Image", image)
    cv.imshow("Rotated Image", rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()