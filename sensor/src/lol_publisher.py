#!/usr/bin/env python

import rospy
from common_msgs.msg import lol

rospy.init_node('lol_publisher')
pub = rospy.Publisher('custom_msg', lol, queue_size=1)
custom_data = lol()
rate = rospy.Rate(2)
count = 0
alphabets_list =['Hello', 'My', 'Name', 'Is', 'Kim', 'Jun', 'Hee']
while not rospy.is_shutdown():
    if count > 6:
        count = 0
    custom_data.alphabets.data = alphabets_list[count]
    custom_data.quat.x = count + 5
    custom_data.quat.y = count / 2
    custom_data.quat.z = count - 10
    custom_data.quat.w = count * 10
    pub.publish(custom_data)
    print "Published strings in list     : ", custom_data.alphabets.data
    print "Published geometry quaternion x: ", custom_data.quat.x
    print "Published geometry quaternion y: ", custom_data.quat.y 
    print "Published geometry quaternion z: ", custom_data.quat.z 
    print "Published geometry quaternion w: ", custom_data.quat.w
    print "Finished publishing"
    count += 1
    rate.sleep()
