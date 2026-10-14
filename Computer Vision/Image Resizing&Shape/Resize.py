import cv2
image = cv2.imread("D:\Computer Vision\opencv_practice.png")
if image is None:
    print("Image not found")
else:
    resized = cv2.resize(image, (300,300))
    cv2.imshow("Original", image)
    cv2.imshow("Resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite("Resized.png",resized)

    
    