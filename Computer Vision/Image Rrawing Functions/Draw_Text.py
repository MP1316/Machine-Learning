import cv2
image = cv2.imread("D:\Computer Vision\Image Rrawing Functions\Python_Image.png.png")
if image is None:
    print("Could not load image:")
else:
    print("Loadoing Image successfully:")

    # cv2.putText(img, text, org(x,y), font, fontscale, color, thickness)

    cv2.putText(image, "Machine Learning", (50,250),
    cv2.FONT_HERSHEY_COMPLEX, 1.3, (255,0,0), 2)
    cv2.imshow("Add Text On the Image:", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
     