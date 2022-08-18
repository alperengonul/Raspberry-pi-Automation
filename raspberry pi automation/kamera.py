import cv2
import numpy as np

capture = cv2.VideoCapture(0)


maske = cv2.createBackgroundSubtractorMOG2(500,750,True)

kare_sayisi = 0

while(1):
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
        print('Hareket algılandı')
        frame_yeni =cv2.rectangle(frame_yeni,(x,y),(x+w,y+h),(0,250,0),2)
        cv2.putText(frame_yeni,'Hareket algılandı',(10,50), cv2.FONT_HERSHEY_SIMPLEX , 1 ,(255,255,255), 2 )
        
   cv2.imshow('Kamera',frame_yeni)
   cv2.imshow('Maske' , yuzey_maske)
    
   k = cv2.waitKey(1) & 0xff
   if k ==27:
    break

capture.release()
cv2.destroyAllWindows()
                                  
       