import cv2
image = cv2.imread("D:\Computer Vision\Image Resizing&Shape\Kl_ Rahul.png")

# syntax

# cv2.GaussianBlur(image, (kernal_size x, kernal size y), sigma )

blured = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow("Original image:", image)
cv2.imshow("Blurred image:", blured)
cv2.waitKey(0)
cv2.destroyAllWindows()
