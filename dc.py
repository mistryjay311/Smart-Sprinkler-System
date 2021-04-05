import RPi.GPIO as GPIO

import time
from time import sleep
import sys
import ibmiotf.application
import ibmiotf.device
import random
organization = "ckhlhg"
deviceType = "Humid1"
deviceId = "007"
authMethod = "use-token-auth"
authToken = "ZnQ8aM)NzY1Zp1XA7V"
try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)#.............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        

Motor1A = 24
Motor1B = 23
Motor1E = 25
 
def setup():
	GPIO.setmode(GPIO.BCM)				 Numbering
	GPIO.setup(Motor1A,GPIO.OUT)  	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
 
def loop():
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
 
	sleep(5)
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
sleep(5)
	
	GPIO.output(Motor1E,GPIO.LOW)

def destroy():	
	GPIO.cleanup()

if __name__ == '__main__':    
	setup()
	try:
    		loop()
  	except KeyboardInterrupt:
		destroy()
