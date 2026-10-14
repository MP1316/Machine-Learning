import cv2
image = cv2.imread("D:\Computer Vision\Image Resizing&Shape\Kl_ Rahul.png")

# syntax

# cv2.MedianBlur(image, kernal_size  )

median_blur = cv2.medianBlur(image,13)
cv2.imshow("Original image:", image)
cv2.imshow("Blurred image:", median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows( )
