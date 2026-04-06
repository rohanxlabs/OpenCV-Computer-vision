import cv2 as cv

image = cv.imread('Photos/cats.jpg')

if image is None:
    print("Image not found")
else:
    print("Image found")
    cv.putText(image,
               text="Hello World",
                org=(50, 300),
                fontFace=cv.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(255, 0, 0),
                thickness=2,
                lineType=cv.LINE_AA)

    cv.imshow("Adding text over image", image)
    cv.waitKey(0)
    cv.destroyAllWindows() 