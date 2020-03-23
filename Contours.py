from cv2 import cv2
import numpy as np
def main() :
    imgpath = "/home/naivedya/Desktop/OpenCV_Logo.png"
    img = cv2.imread(imgpath)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, contours, -1, (50,50,50), 4)
    cv2.imshow('Drawing Contours', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
