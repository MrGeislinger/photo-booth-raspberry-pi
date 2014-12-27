import RPi.GPIO as GPIO

#Global variables
buttonLED = {'BCM':None, 'BOARD':None} #pin number for each mode

#Set button LED pin number
def setButtonLED(mode,pin):
	#Check the mode given is valid
	if mode in buttonLED.keys():
		buttonLED[mode] = pin
		return True
	else:
		return False

#Switch LED on or off (True or False respectively passed in)
def buttonLED(on):
	if on:
		GPIO.output(buttonLED,GPIO.HIGH)
	else:
		GPIO.output(buttonLED,GPIO.LOW)
	#Returns that the power has been switched
	return not on

#
