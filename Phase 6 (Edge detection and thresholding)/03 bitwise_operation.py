"""
Bitwise operations
1. cv.bitwise_and(img1, img2)
2. cv.bitwise_or(img1, img2)
3. cv.bitwise_not(img)
"""

import cv2 as cv
import numpy as np

img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

cv.circle(img1, (150, 150), 100, 255, -1)
cv.rectangle(img2, (100, 100), (250, 250), 255, -1)

bitwise_and = cv.bitwise_and(img1, img2)
bitwise_or = cv.bitwise_or(img1, img2)
bitwise_not = cv.bitwise_not(img1)

cv.imshow("Circle", img1)
cv.imshow("Rectangle", img2)
cv.imshow(" AND", bitwise_and)
cv.imshow(" OR", bitwise_or)
cv.imshow(" NOT", bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()