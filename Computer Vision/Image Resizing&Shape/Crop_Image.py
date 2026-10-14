import cv2
image = cv2.imread("D:\Computer Vision\Image Resizing&Shape\Kl_ Rahul.png.png")
cropped = image[100:300, 50:250]
cv2.imshow("Real image", image)
cv2.imshow("Cropped image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
