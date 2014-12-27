#Import neccessary modules
import numpy as np
import cv2

#Input capture from camera
video = cv2.VideoCapture(0)

#Display video
while(True):
	#Frame-by-frame capture
	_ , frame = video.read()

	#Frame operations
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	#Dispaly the frame\
	cv2.imshow('frame',gray)

	#To quit, press 'q'
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#Release the video capture
video.release()
cv2.dstroyAllWindows()
