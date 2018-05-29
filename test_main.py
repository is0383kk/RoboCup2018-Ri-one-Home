#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from time import sleep
import sys
import rospy
from std_msgs.msg import String

	
def function1():
	print("success")

def topicDetector():
	# This is a roop function, so it continues to roop, until topic is received
	print("I am waiting for the next message.")
	rospy.Subscriber("messenger", String, callback)


def callback(msg):
	face_cut = rospy.Publisher("face_cut", String, queue_size=10, latch=True)
	print(msg.data)
	if(msg.data == "turned"):
		print("turned")
	elif(msg.data == "face"):
		print("face")
		start.publish("face_cut")
		
if __name__ == '__main__':
	rospy.init_node("spr_main")
	# Speach and personal recognision start.

	os.system('espeak "{I want to play a riddle game}" -s 90')
	print("SPR start")

	os.system('espeak "{I will wait for 10 seconds}" -s 90')
	print("Waiting for 10 seconds")

	# Specify waiting time
	sleep(10)
	start = rospy.Publisher("start", String, queue_size=10, latch=True)
	start.publish("start")# SPR starts
	
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		topicDetector()
		rate.sleep()
