############################
# RaspberryPi Camera       # 
############################
import picamera


#Start the PiCamera instance
def startCamera(resolutionX, resolutionY, vflip=False, hflip=False):
	#Start camera
	camera = picamera.PiCamera()
	camera.resolution = (resolutionX, resolutionY) 
	camera.vflip = vflip
	camera.hflip = hflip
	return camera

#Take the (count)th picture and then returns an incremented count
def takePicture(count=0, photoName='photo', photoExt='jpg', 
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