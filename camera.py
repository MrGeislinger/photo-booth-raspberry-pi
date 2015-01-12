############################
# RaspberryPi Camera       # 
############################
import picamera
from time import sleep, strftime, gmtime
import subprocess

#Start the PiCamera instance
def startCamera(resolutionX, resolutionY, vflip=False, hflip=False):
	#Start camera
	camera = picamera.PiCamera()
	camera.resolution = (resolutionX, resolutionY) 
	camera.vflip = vflip
	camera.hflip = hflip
	return camera

#Take the (count)th picture and then returns an incremented count
def takePicture(camera, count=0, photoName='photo', photoExt='jpg', 
	            prepMessage='',postMessage=''):
	#Print the preparation message 
    print(prepMessage)
    #Take a picture saving as name_count.extension
    camera.capture('%s_%d.%s' %(photoName,count,photoExt))
    #Print the post-capture message
    print(postMessage)
    #Increment the count and return
    return (count+1)

#Begin to show camera preview
def startPreview(camera):
	camera.start_preview()

#Stop showing the camera preview
def stopPreview(camera):
	camera.stop_preview()

#Overlay variables
OVERLAY_WAITING = "Push the Button to Start Taking Pictures"
OVERLAY_PREP    = "Camera Will Take 3 Pictures"
OVERLAY_READY   = "Pose & Get Ready in: "
OVERLAY_CAPTURE = "Smile! :)"
OVERLAY_NEXT    = "Get Ready for the Next Photo..."
OVERLAY_DONE    = "Your photos will later be on our website VictorPlusEmily.com! Don't forget to sign the guestbook!"

#Run a procedure when signal to start the photo booth procedure
def startPhotoBooth(camera):
	#User pushes button, shows a different overlay
	camera.annotate_text = OVERLAY_PREP
	sleep(3)

	#Make directory
	dirName = strftime('%j-%H-%M-%S',gmtime())
	subprocess.call(['mkdir',dirName])
	#Take three photos
	totalPhotos = 3
	for photoNum in range(totalPhotos):
		#Preparing to take picture
		countdown = 5 #5 seconds to countdown from
		for i in range(countdown):
			camera.annotate_text = OVERLAY_READY + str(countdown-i)
			sleep(1)
		#Let people know picture is now being taken
		camera.annotate_text = OVERLAY_CAPTURE
		captureTime = 0.5 #Give a little time to be warned
		sleep(captureTime) 
		#Take picture
		camera.annotate_text = '' #Remove annotation so it doesn't show in picture
		camera.hflip = False
		phName = dirName + '/photo'
		takePicture(camera,count=photoNum,photoName=phName)
		#Prepare for the next photo (if applicable)
		camera.hflip = True
		photoNum += 1
		if photoNum < totalPhotos:
			#Prepare for the next photo
			camera.annotate_text = OVERLAY_NEXT
			nextWaitTime = 1 
		else:
			camera.annotate_text = OVERLAY_DONE
			#
			subprocess.call(['montage', dirName+'/photo*', '-tile', '1x3', '-geometry','+3+0',
                                         '-border', '+10+5', '-bordercolor', 'gray', '-resize', '300x400', #'500x900',
                                          dirName+'/temp.jpg'])
			subprocess.call(['montage', dirName+'/temp.jpg', dirName+'/temp.jpg', '-tile','2x1', 
					 '-geometry','+20+0', dirName+'/final.jpg'])
			#
			nextWaitTime = 25
			#
		#Give a little break for the next step
		#Print
		#subprocess.call(['lp','-d', 'Canon_MP495_series',dirName+'/final.jpg'])
		sleep(nextWaitTime)
	#Reset the camera's overlay back
	camera.annotate_text = OVERLAY_WAITING
	return camera