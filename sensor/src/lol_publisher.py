#!/usr/bin/env python

import rospy
from common_msgs.msg import lol
from common_msgs.srv import BatteryCost, BatteryCostRequest

rospy.init_node('lol_publisher')
pub = rospy.Publisher('custom_msg', lol, queue_size=1)
custom_data = lol()


requester = rospy.ServiceProxy('battery_cost', BatteryCost)

rate = rospy.Rate(2)
count = 0
battery_count = 0
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

    battery_cost = 4 * battery_count
    if battery_cost % 5 == 0:
        request = BatteryCostRequest(cost=battery_cost)
        response = requester(request)
        print "================================Service Test=========================="
        print "Battery cost : ", request.cost
        print "Remained battery : ", response.remain
        if response.remain == 0:
            print "Battery needs to be charged"
        print "======================================================================"
    battery_count += 1
    if battery_count > 25:
        battery_count = 0
    rate.sleep()
