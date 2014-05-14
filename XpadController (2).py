 #!/usr/bin/python
# Requires lego-pi project from https://github.com/zephod/lego-pi
# good tutorial http://mattdyson.org/blog/2013/01/using-an-xbox-360-wireless-controller-with-raspberry-pi/
# sudo pip install websocket-client

from websocket import create_connection
from threading import Thread
import socket
from datetime import datetime
import sys
import time
from legopi.lib import xbox_read

#HOST = "192.168.1.72"
#PORT = 8934

print "established connection2"
s = create_connection("ws://127.0.0.1:50007")

#s.settimeout()
print "established connection"
def burstGPIO(delay): 
	while True:
		if switch == "A":
			while Abool:
				time.sleep(delay)
				s.send("forward")
				print "ABurst"
			break
		elif switch == "B":
			while Bbool:
				time.sleep(delay)
				s.send("back")
				print "BBurst"
			break
		elif switch == "LB":
			while LBbool:
				time.sleep(delay)
				s.send("left")
				print "LBBurst"
			break
		elif switch == "RB":
			while RBbool:
				time.sleep(delay)
				s.send("right")
				print "RBBurst"
			break
		time.sleep(0.1)
			   

global LBbool
global RBbool
global Abool
global Bbool
global switch

switch = "none"
LBbool = False
RBbool = False
Abool = False
Bbool = False


#Starts the threads sending the burst signals


   
#Iterates through the key presses of the xbox controller
for event in xbox_read.event_stream(deadzone=12000):
	if event.key == "A":
		if event.value == 1: 
			switch = "A"
			Abool = True
			Thread(target=burstGPIO, args=(0.2,)).start()
			s.send("forward")
			s.ping()
		else: 
			Abool = False
			switch = "none"
	if event.key == "B":
		if event.value == 1: 
			switch = "B"
			Bbool = True
			Thread(target=burstGPIO, args=(0.2,)).start()
			s.send("back")
		else: 
			Bbool = False
			switch = "none"
		
	if event.key == "RB":
		if event.value == 1:
			switch = "RB" 
			RBbool = True
			Thread(target=burstGPIO, args=(0.2,)).start()
			s.send("right")
		else: 
			RBbool = False
			switch = "none"
	if event.key == "LB":
		if event.value == 1: 
			switch = "LB"
			LBbool = True
			Thread(target=burstGPIO, args=(0.2,)).start()
			s.send("left")
		else: 
			LBbool = False
			switch = "none"
	#print event