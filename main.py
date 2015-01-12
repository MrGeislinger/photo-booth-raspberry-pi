#
import os
import time
import camera
import button
import RPi.GPIO as GPIO

#Camera setup
cam = camera.startCamera(1200,960,hflip=True) #Flip vertically
cam.annotate_text = camera.OVERLAY_WAITING
camera.startPreview(cam)

#Button setup
GPIO.setmode(GPIO.BOARD)
#led = 0 
but = 7
GPIO.setup(but,GPIO.IN, pull_up_down = GPIO.PUD_UP)

#camera.startPhotoBooth(cam)

#Always running background
while(True):
	#Show the basic screen
	#If button is pressed
	inp = GPIO.input(7)
	if inp == False:
		camera.startPhotoBooth(cam)
	
	
