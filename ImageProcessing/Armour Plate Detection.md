from cv2 import cv2
from PIL import Image
from pylab import *

# robot = Image.open("Desktop/robot.jpg")
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
# cv2.drawContours(robotq, contours, 16, (0,255,0), thickness = 10)
cv2.line(robotq, (1945, 1728), (2335,1670), (0,255,0), 10)
cv2.line(robotq, (1945, 1728), (1975, 1910), (0,255,0), 10)
cv2.line(robotq, (1975, 1910), (2370, 1840), (0,255,0), 10)
cv2.line(robotq, (2335,1670), (2370, 1840), (0,255,0), 10)
# print(contours[16])
figure()
imshow(robotq)
axis('off')
show()
