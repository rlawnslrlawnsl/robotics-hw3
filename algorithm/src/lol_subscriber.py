#!/usr/bin/env python

import rospy
from common_msgs.msg import lol
from common_msgs.srv import BatteryCost, BatteryCostResponse

def service_callback(request):
    full_battery = 100
    reamin_battery = full_battery - request.cost
    response = BatteryCostResponse(remain=reamin_battery)
    print "Battery cost : ", request.cost
    print "Remained battery : ", response.remain
    return response


def quaternion_alphabet(msg):
    print "Subscribed strings: ", msg.alphabets.data
    print "Subscribed geometry quaternion x: ", msg.quat.x
    print "Subscribed geometry quaternion y: ", msg.quat.y
    print "Subscribed geometry quaternion z: ", msg.quat.z
    print "Subscribed geometry quaternion w: ", msg.quat.w
    print "Finished publishing"

rospy.init_node('lol_subscriber')
sub = rospy.Subscriber('custom_msg', lol, quaternion_alphabet)
service = rospy.Service('battery_cost', BatteryCost, service_callback)
rospy.spin()
