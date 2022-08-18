
import RPi.GPIO as GPIO
import time

sensor = 12
buzzer = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)



try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,False)
          print("Object Detected")
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,True)


except KeyboardInterrupt:
    GPIO.cleanup()