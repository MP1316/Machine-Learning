import cv2
# print(cv2.__version__)

image = cv2.imread("D:\Computer Vision\opencv_practice.png")
if image is None:
    print("Error: Image not found")
else:
    print("Image load successfully")    
