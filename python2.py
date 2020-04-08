#!/usr/bin/env python3

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def image_converter():
	
	rospy.init_node('node2',anonymous = True)
	image_sub = rospy.Subscriber("/camera/depth/image_raw",Image,callback)
	rospy.spin()
 	
def callback(data):
	bridge = CvBridge()
	try:
		cv_img = bridge.imgmsg_to_cv2(data,desired_encoding = 'passthrough')
	except CvBridgeError as e:
		print(e)
	cv2.imshow("image window",cv_img)
	cv2.waitKey(0)
	cv2.destryAllWindows()
	

if __name__=='__main__':
	image_converter()
