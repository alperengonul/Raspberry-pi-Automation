# from Seeed Studio Wiki
# http://wiki.seeed.cc/Raspberry_Pi_Relay_Board_v1.0/
import RPi.GPIO as GPIO
import time
import signal
import sys
import smbus
import cv2
import numpy as np


sensor = 12
kapi=7



# Ir sensor kodları


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(16,GPIO.OUT)

GPIO.output(16,False)

# Ir sensor kodları

#servo tanımı
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
servo1.start(0)

#servo tanımı
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)







bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)


class Relay():
    global bus

    def __init__(self):
        self.DEVICE_ADDRESS = 0x20  # 7 bit address (will be left shifted to add the read write bit)
        self.DEVICE_REG_MODE1 = 0x06
        self.DEVICE_REG_DATA = 0xff
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_1(self):
        print('ON_1...')
        self.DEVICE_REG_DATA &= ~(0x1 << 0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_2(self):
        print('ON_2...')
        self.DEVICE_REG_DATA &= ~(0x1 << 1)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_3(self):
        print('ON_3...')
        self.DEVICE_REG_DATA &= ~(0x1 << 2)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_4(self):
        print('ON_4...')
        self.DEVICE_REG_DATA &= ~(0x1 << 3)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_1(self):
        print('OFF_1...')
        self.DEVICE_REG_DATA |= (0x1 << 0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_2(self):
        print('OFF_2...')
        self.DEVICE_REG_DATA |= (0x1 << 1)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_3(self):
        print('OFF_3...')
        self.DEVICE_REG_DATA |= (0x1 << 2)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_4(self):
        print('OFF_4...')
        self.DEVICE_REG_DATA |= (0x1 << 3)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ALLON(self):
        print('ALL ON...')
        self.DEVICE_REG_DATA &= ~(0xf << 0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ALLOFF(self):
        print('ALL OFF...')
        self.DEVICE_REG_DATA |= (0xf << 0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)


if __name__ == "__main__":
    relay = Relay()

    # Called on process interruption. Set all pins to "Input" default mode.
    def endProcess(signalnum=None, handler=None):
        relay.ALLOFF()
        sys.exit()


    signal.signal(signal.SIGINT, endProcess)




#Ir arac sorgutry:

#Ir arac sorgu
    
#kapi sensor sorgu
   
#kamera kodları
capture = cv2.VideoCapture(0)


maske = cv2.createBackgroundSubtractorMOG2(500,750,True)

kare_sayisi = 0


while True:
   
   ret,frame = capture.read()
   
   if not ret:
       break
    
    
   kare_sayisi += 1
    
   frame_yeni = cv2.resize(frame,(0,0),fx=1,fy=1)
    
   yuzey_maske = maske.apply(frame_yeni)
    
   pixelsayaci = np.count_nonzero(yuzey_maske)
    
   print('Görüntü:%d,Değişen pixel sayısı:%d'% (kare_sayisi,pixelsayaci))
    
   x,y,w,h =cv2.boundingRect(yuzey_maske)
    
   if(kare_sayisi > 1 and pixelsayaci >500):
        GPIO.output(16, True)
        frame_yeni =cv2.rectangle(frame_yeni,(x,y),(x+w,y+h),(0,250,0),2)
        cv2.putText(frame_yeni,'Hareket algılandı',(10,50), cv2.FONT_HERSHEY_SIMPLEX , 1 ,(255,255,255), 2 )
   else:
        GPIO.output(16, False)
        
   cv2.imshow('Kamera',frame_yeni)
   cv2.imshow('Maske' , yuzey_maske)
    
   k = cv2.waitKey(1) & 0xff
   if k ==27:
    break

   GPIO.input(sensor)
   if GPIO.input(7)==1 :
       relay.ON_1()
   elif GPIO.input(7) ==0 :
       relay.OFF_1()
   if GPIO.input(sensor)==1:
       relay.ON_2()
       servo1.ChangeDutyCycle(7)
   elif GPIO.input(sensor)==0:
       servo1.ChangeDutyCycle(1)
       print("arac geldi")
       

capture.release()
cv2.destroyAllWindows()
#kamera kodları


#kapi sensor sorgu

#while True:
  #GPIO.input(sensor)
  #if GPIO.input(7)==1 :
    #  relay.ON_1()
  #elif GPIO.input(7) ==0 :
    #  relay.OFF_1()
  #if GPIO.input(sensor):
      #relay.ON_2()
     # servo1.ChangeDutyCycle(7)
      #time.sleep(0.5)
  #else:
     # servo1.ChangeDutyCycle(1)
      #print("arac geldi")
     # time.sleep(2)

       
     
        

           
                     



