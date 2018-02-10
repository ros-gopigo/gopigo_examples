#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import time

def main():
    rospy.init_node('led_publisher')

    pub_led_left = rospy.Publisher('led_left', Bool, queue_size=1)
    pub_led_right = rospy.Publisher('led_right', Bool, queue_size=1)

    msg = Bool()

    # activate left LED
    msg.data = True
    pub_led_left.publish(msg)

    time.sleep(2)

    # deactivate left LED
    msg.data = False
    pub_led_left.publish(msg)

    time.sleep(0.5)

    # activate right LED
    msg.data = True
    pub_led_right.publish(msg)

    time.sleep(2)

    # deactivate right LED
    msg.data = False
    pub_led_right.publish(msg)

if __name__ == '__main__':
    main()