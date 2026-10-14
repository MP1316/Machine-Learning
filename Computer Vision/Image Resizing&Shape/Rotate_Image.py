import cv2
image = cv2.imread("vD:\Computer Vision\Image Resizing&Shape\Kl_ Rahul.png.png")
if image is not None:
    (h,w) = image.shape[:2]
    center = (h//2, w//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(image, M, (h,w))
    cv2.imshow("Original", image)
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Loading successfully:")

else:
    print("Could not load image:")
    