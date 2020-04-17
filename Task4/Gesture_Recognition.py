#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import numpy as np
import cv2

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    video = cv2.VideoCapture(0)
    lower_skin = np.array([30,0,0])
    upper_skin = np.array([200,30,30])
    a = 0
    w = 1
    while True:

        a = a + 1
        check,frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = cv2.inRange(frame, lower_skin, upper_skin) 
        overlap = cv2.bitwise_and(frame,frame, mask= mask)
        imgray = cv2.cvtColor(overlap, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 0, 255, 0)
        image, contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for c in contours:
            if cv2.contourArea(c)>4000:
            	M = cv2.moments(c)
            	cx = int(M['m10']/M['m00'])
                if a == w:
                    c1 = cx
                            
                if a == w + 5:
                    c2 = cx
                    w = w + 10
                    if c2-c1 > 30:
                        # print("LEFT!")
                        vel_msg.linear.x = -abs(5)
                    elif c1- c2 > 30:
                        # print("RIGHT!")
                        vel_msg.linear.x = abs(5)
                    else:
                        continue
                    vel_msg.linear.y = 0
                    vel_msg.linear.z = 0
                    vel_msg.angular.x = 0
                    vel_msg.angular.y = 0
                    vel_msg.angular.z = 0  
                    # while not rospy.is_shutdown():
    
                    #Setting the current time for distance calculus
                    t0 = rospy.Time.now().to_sec()
                    current_distance = 0
    
                    #Loop to move the turtle a specified distance
                    while(current_distance < 2):
                        #Publish the velocity
                        velocity_publisher.publish(vel_msg)
                        #Takes actual time to velocity calculus
                        t1=rospy.Time.now().to_sec()
                        #Calculates distancePoseStamped
                        current_distance= 5*(t1-t0)
                    #After the loop, stops the robot
                    vel_msg.linear.x = 0
                    #Force the robot to stop
                    velocity_publisher.publish(vel_msg)  
                    
                # cv2.drawContours(overlap, contours, c, (255,255,255), 4)
        # cv2.imshow("Capturing", overlap)
        # key = cv2.waitKey(1)
        # if key == ord('q'):
        #     break;
        
    video.release()
    # cv2.destroyAllWindows
        
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
