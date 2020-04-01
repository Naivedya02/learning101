from cv2 import cv2
import numpy as np
from pylab import *
def main():
    img = cv2.imread("/home/naivedya/Desktop/Sudoku.png")        
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    
    i = 0
    for i in range(len(lines)):
        for rho,theta in lines[i]:
            i+=1
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1200*(-b))
            y1 = int(y0 + 1200*(a))
            x2 = int(x0 - 1200*(-b))
            y2 = int(y0 - 1200*(a))

            cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)

    figure()
    imshow(img)
    axis('off')
    show()
    
if __name__=="__main__":
    main()