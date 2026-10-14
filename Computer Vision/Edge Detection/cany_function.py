import cv2
image = cv2.imread("D:\Computer Vision\Image Resizing&Shape\Kl_ Rahul.png", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50, 150)

cv2.imshow("Original image", image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
