import RPi.GPIO as GPIO

#Global variables
buttonLED = 0 #pin number for button's LED

#Switch LED on or off (True or False respectively passed in)
def buttonLED(on):
	if on:
		GPIO.output(buttonLED,GPIO.HIGH)
	else:
		GPIO.output(buttonLED,GPIO.LOW)
	return not on

