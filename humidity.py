Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import RPi.GPIO as GPIOimport dht11GPIO.setwarnings(False)GPIO.setmode(GPIO.BCM)GPIO.cleanup()instance = dht11.DHT11(pin = 14)result = instance.read()if result.is_valid():    print("Temperature: %-3.1f C" % result.temperature)    print("Humidity: %-3.1f %%" % result.humidity)else:    print("Error: %d" % result.error_code)