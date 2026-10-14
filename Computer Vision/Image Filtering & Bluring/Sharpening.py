import cv2
import numpy as np
image = cv2.imread("D:\Computer Vision\Image Resizing&Shape\Kl_ Rahul.png")

# syntax

# cv2.filter2d(image, ddepth, kernal )

sharpened_kernal = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(image, -1, sharpened_kernal )
cv2.imshow("Original image:", image)
cv2.imshow("Sharpened image:", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
 