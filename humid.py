import RPi.GPIO as GPIO
import dht11

import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
organization = "ckhlhg"
deviceType = "Humid1"
deviceId = "007"
authMethod = "use-token-auth"
authToken = "ZnQ8aM)NzY1Zp1XA7V"


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin = 14)
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)

