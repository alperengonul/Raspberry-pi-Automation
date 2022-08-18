# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)

#Let's move the servo!
print ("Rotating 180 degrees in 10 steps")

# Define variable duty

# Loop for duty values from 2 to 12 (0 to 180 degrees)


# Wait a couple of seconds

# Turn back to 90 degrees


#turn back to 0 degrees
print ("Turning back to 0 degrees")
servo1.ChangeDutyCycle(1)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo1.ChangeDutyCycle(7)
time.sleep(0.5)

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye")
