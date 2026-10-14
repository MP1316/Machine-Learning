import cv2
image = cv2.imread("D:\Computer Vision\Image Resizing&Shape\Kl_ Rahul.png.png")
if image is not None:
    print("Image load successfully")
    resized = cv2.resize(image, (300,300))
    flipped_vertically = cv2.flip(resized, 0)
    flipped_horizontally = cv2.flip(resized, 1)
    flipped_both = cv2.flip(resized, -1)

    cv2.imshow("Original", resized)
    cv2.imshow("Flipped Vertically", flipped_vertically)
    cv2.imshow("Flipped Horizontally", flipped_horizontally)
    cv2.imshow("flipped Both", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Could not load image")

