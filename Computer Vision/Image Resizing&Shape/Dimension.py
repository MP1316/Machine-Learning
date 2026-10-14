import cv2
image = cv2.imread("D:\Computer Vision\opencv_practice.png")
if image is not None:
    h,w,c = image.shape
    print(f"Image loaded: \nheight:{h}\n 'width:{w}\n 'channel:{c}")
else:
    print("Not loaded")    

    