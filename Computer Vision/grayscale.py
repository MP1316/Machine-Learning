import cv2
image = cv2.imread("D:\Computer Vision\opencv_practice.png")
if image is not None:
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Greyscale image", grey)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not load image")   
     