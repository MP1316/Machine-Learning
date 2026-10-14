import cv2
image = cv2.imread("D:\Computer Vision\Image Rrawing Functions\Python_Image.png.png")
if image is None:
    print("Could not load image:")
else:
    print("Loadoing Image successfully:")

    center = (200,200)
    radius = 100
    color = (0,255,0)
    thickness = -1

    cv2.circle(image, center, radius, color, thickness)
    cv2.imshow("Draw Circle:", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
     