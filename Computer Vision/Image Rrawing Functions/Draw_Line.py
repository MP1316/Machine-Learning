import cv2
image = cv2.imread("D:\Computer Vision\Image Rrawing Functions\Python_Image.png.png")
if image is None:
    print("Ooops! Your python image is not working:")

else:
    print("Image load successfully:")

    plt1 = (50,100)
    plt2 = (300,100)
    color = (255,0,0)
    thickness = 5

    cv2.line(image, plt1, plt2, color, thickness)
    cv2.imshow("Line Drawing:", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
     
