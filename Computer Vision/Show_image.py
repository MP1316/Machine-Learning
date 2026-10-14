import cv2
image = cv2.imread("D:\Computer Vision\opencv_practice.png")
if image is not None:
    cv2.imshow("Image shiwing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could naot show nimage") 
    