#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node") #always initialize, otherwise you cannot use ros functionality
    rospy.loginfo("Test node has been started.")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep() #makes loop repeated with 10Hz freq.
