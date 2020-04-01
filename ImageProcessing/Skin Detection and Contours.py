from cv2 import cv2
import numpy as np


def main() :
    lower_skin = np.array([3,25,40])
    upper_skin = np.array([18,255,255])
    imgpath = "/home/naivedya/Desktop/Hands and Skins/Skin(3).jpg"
    img = cv2.imread(imgpath)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Here we are defining range of skin  color in HSV 
    # This creates a mask of skin coloured objects found in the image. 
    mask = cv2.inRange(hsv, lower_skin, upper_skin) 
    overlap = cv2.bitwise_and(hsv,hsv, mask= mask)
    bgr = cv2.cvtColor(overlap, cv2.COLOR_HSV2BGR)
    cv2.imshow('Original Image', img)
    cv2.imshow('Skin Detection', bgr)
    # cv2.imshow('Image in HSV',hsv) 
    # cv2.imshow('Mask',mask)
    imgray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 80, 255, 0)
    contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(bgr, contours, -1, (45,150,48), 4)
    cv2.imshow('Drawing Contours', bgr)
    # cv2.imshow('Threshold', thresh) 
    # Destroys all of the HighGUI windows on pressing any keyboard key 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
