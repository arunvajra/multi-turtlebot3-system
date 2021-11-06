#!/usr/bin/env
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist 

def callback(dt):
    
    thr1 = 0.8 # Laser scan range threshold
    thr2 = 0.8
    if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2: # Checks if there are obstacles in front 

        move.linear.x = 0.5 # go forward (linear velocity)
        move.angular.z = 0.0 # do not rotate (angular velocity)
    else:
        move.linear.x = 0.0 # stop
        move.angular.z = 0.5 # rotate counter-clockwise
        if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2:
            move.linear.x = 0.5
            move.angular.z = 0.0
    pub.publish(move) # publish the move object


move = Twist() # Creates a Twist message type object
rospy.init_node('robot10_node') # Initializes a node
pub = rospy.Publisher('/tb3_9/cmd_vel', Twist, queue_size=10)  # Publisher 

sub = rospy.Subscriber('/tb3_9/scan', LaserScan, callback)  # Subscriber 
						      
rospy.spin() # Loops infinitely until someone stops the program execution
