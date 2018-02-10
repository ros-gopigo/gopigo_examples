#!/usr/bin/env python
import rospy
from std_srvs.srv import Trigger
import time

def main():
    rospy.init_node('led_client')

    srv_led_on_left = rospy.ServiceProxy('led_on_left', Trigger)
    srv_led_on_right = rospy.ServiceProxy('led_on_right', Trigger)
    srv_led_off_left = rospy.ServiceProxy('led_off_left', Trigger)
    srv_led_off_right = rospy.ServiceProxy('led_off_right', Trigger)

    srv_led_on_left(); time.sleep(2)
    srv_led_off_left(); time.sleep(2)
    srv_led_on_right(); time.sleep(2)
    srv_led_off_right(); time.sleep(2)

if __name__ == '__main__':
    main()