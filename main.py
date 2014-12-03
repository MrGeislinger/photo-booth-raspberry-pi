import RPi.GPIO as GPIO
import picamera
import time

# blinking function
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
pinsBOARD = {'a':35, 'b':33, 'c':31, 'd':38, 
             'e':40, 'f':32, 'g':36, 'h':29}
pins = pinsBOARD
nums = [
        ['a','b','c','d','e','f'    ], #0
        [    'b','c'                ], #1
        ['a','b',    'd','e',    'g'], #2
        ['a','b','c','d',        'g'], #3
        [    'b','c',        'f','g'], #4
        ['a',    'c','d',    'f','g'], #5
        ['a',    'c','d','e','f','g'], #6
        ['a','b','c'                ], #7
        ['a','b','c','d','e','f','g'], #8
        ['a','b','c',        'f','g'], #9
        []  #NONE
]


# Setup GPIO
for p in pins.values():
    GPIO.setup(p, GPIO.OUT)

# Flash all the LED segments for a given number definition
def numLedOn(numSegments):
    for segment in numSegments:
        GPIO.output(pins[segment],GPIO.HIGH)
    return

def numLedOff(numSegments):
    for segment in numSegments:
        GPIO.output(pins[segment],GPIO.LOW)
    return

def flashNum(num,flashTime):
    print "Flashing %d for %.2f seconds" %(num,flashTime)
    #Test that the number can be displayed (one digit)
    if num in range(10):
        numLedOn(nums[num])
        time.sleep(flashTime)
        numLedOff(nums[num])
    else:
        print "Not defined"
    return

#Countdown from a number to another for a given time (flash LED)
def countdownFrom(num,to=0,flashTime=1):
    while num >= to:
        flashNum(num,flashTime)
        num -= 1 # decrease the next number to show

def takePicture(count):
# Camera warm-up time
    print "Picture Being Taken..."
    camera.capture('foo%d.jpg' %count)
    print "Picture was taken!!"
    count += 1
    return count


#Press down button
butPin = 12 # Broadcom pin 18 (P1 pin 12)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
#Press down button
butPinOff = 11 # Broadcom pin 18 (P1 pin 12)
GPIO.setup(butPinOff, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

#Buzzer
buzzPin = 37
GPIO.setup(buzzPin, GPIO.OUT)
def buzzerOn():
    GPIO.output(buzzPin,GPIO.HIGH)
    return
#
def buzzerOff():
    GPIO.output(buzzPin,GPIO.LOW)
    return



#count number of photos
count = 0

#
print("Here we go! Press CTRL+C to exit")
#Start camera
camera = picamera.PiCamera()
camera.vflip = True
camera.start_preview()
camera.resolution = (1024, 768)

try:
    while True:
        input_state = GPIO.input(butPin)
        input_state_off = GPIO.input(butPinOff)
        # Stop the camera!!!
        if input_state_off == False:
            print 'endddd'
            raise KeyboardInterrupt('test')
        if input_state == False:
            print('Button Pressed')
            countdownFrom(3)
            buzzerOn()
            time.sleep(0.2)
            count = takePicture(count)
            buzzerOff()
        # else: # button is pressed:
        #     print "test"
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO



# countdownFrom(10,flashTime=2.5)

# GPIO.cleanup() 


