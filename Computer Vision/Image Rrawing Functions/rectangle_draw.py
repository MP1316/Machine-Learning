import cv2
image = cv2.imread("D:\Computer Vision\Image Rrawing Functions\Python_Image.png.png")
if image is None:
    print("Could not load image:")
else:
    print("Loadoing Image successfully:")

    plt1 = (50,100)
    plt2 = (150,300)
    color = (0,255,0)
    thickness = 5

    cv2.rectangle(image, plt1, plt2, color, thickness)
    cv2.imshow("Rectangle Image:", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
     