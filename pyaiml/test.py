#!/usr/bin/env python
import os
import rospy
import time
import aiml
import sys
from std_msgs.msg import String
# Create a Kernel object.
rospy.init_node('aiml_server')
kernel = aiml.Kernel()
response_publisher= rospy.Publisher('/output',String,queue_size = 10)#pub to text_to_speech
def callback(data):
	x = data.data
	print(kernel.respond(x))
        time.sleep(10)
	response = kernel.respond(x)
	response_publisher.publish(response)
def listener():
	rospy.Subscriber("/key",String, callback)
	rospy.spin()
if __name__=='__main__':
	kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
	kernel.saveBrain("standard.brn")
	listener()



