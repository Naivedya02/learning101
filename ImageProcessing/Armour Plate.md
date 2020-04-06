from cv2 import cv2
from PIL import Image
from pylab import *
import numpy as np

robot = cv2.imread("Desktop/robot.jpg")
lower_skin = np.array([0,0,220])
upper_skin = np.array([40,130,255])

robotp = cv2.cvtColor(robot, cv2.COLOR_BGR2HSV)
robotq = cv2.cvtColor(robot, cv2.COLOR_BGR2RGB)

mask = cv2.inRange(robotp, lower_skin, upper_skin) 
overlap = cv2.bitwise_and(robotp,robotp, mask= mask)
gray = cv2.cvtColor(overlap,cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(gray, 80, 255, 0)
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

i = 0
sumx1 = 0
sumx2 = 0
min1 = 10000
min2 = 10000
max1 = 0
max2 = 0

for c in range(len(contours)):
    if cv2.contourArea(contours[c]) < 500:
        continue
    i+=1
       
    if i == 1:
        for h in range(len(contours[c])):
            sumx1 += contours[c][h][0][0]
            if contours[c][h][0][1] > max1:
                max1 = contours[c][h][0][1]
            if contours[c][h][0][1] < min1:
                min1 = contours[c][h][0][1] 
        avg1 = sumx1//len(contours[c])
    if i == 2:
        for h in range(len(contours[c])):
            sumx2 += contours[c][h][0][0]
            if contours[c][h][0][1] > max2:
                max2 = contours[c][h][0][1]   
            if contours[c][h][0][1] < min2:
                min2 = contours[c][h][0][1]           
        avg2 = sumx2//len(contours[c])

pts = np.array([[avg1,min1],[avg2,min2],[avg2,max2],[avg1,max1]])
pts = pts.astype(np.int32)
pts = pts.reshape((-1,1,2))
robotq = cv2.polylines(robotq,[pts],True,(0,255,0), thickness=10)

figure()
imshow(robotq)
axis('off')
show()
