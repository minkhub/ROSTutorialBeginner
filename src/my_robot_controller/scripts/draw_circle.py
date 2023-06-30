#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist    # import twist msg from the msg folder of the geometry_msgs package
#added a new package(geo-), so we need to add it to the dependencies(package.xml file)

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started.")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10) #super important; need to give an exact name

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        # publish cmd_vel
        msg = Twist()
        msg.linear.x = 2.0    # turtle head
        msg.angular.z = 1.0
        pub.publish(msg)    # publisher publishing msg
        rate.sleep()