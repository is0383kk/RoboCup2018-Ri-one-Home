#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
from std_msgs.msg import String

def function1():
	print("success")

def function2():
	print("function2")

def topicDetector():
	# ここが無限ループで実行される
	print("hogehoge")
	rospy.Subscriber("messenger", String, callback)


def callback(msg):
	print(msg.data)
	if(msg.data == "turned"):
		function1()
	if(msg.data == "bye"):
		function2()

if __name__ == '__main__':
	rospy.init_node("main")
	start = rospy.Publisher("start", String, queue_size=10, latch=True)
	start.publish("start")
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		topicDetector()
		rate.sleep()