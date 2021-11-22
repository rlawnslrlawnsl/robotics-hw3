#!/usr/bin/env python

import rospy
from common_msgs.msg import lol

def quaternion_alphabet(msg):
    print "Subscribed strings: ", msg.alphabets.data
    print "Subscribed geometry quaternion x: ", msg.quat.x
    print "Subscribed geometry quaternion y: ", msg.quat.y
    print "Subscribed geometry quaternion z: ", msg.quat.z
    print "Subscribed geometry quaternion w: ", msg.quat.w
    print "Finished publishing"

rospy.init_node('lol_subscriber')
sub = rospy.Subscriber('custom_msg', lol, quaternion_alphabet)
rospy.spin()
