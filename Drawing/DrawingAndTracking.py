import cv2
import numpy as np

def dibujar(mask, color):
    contornos,hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 300:
            x,y,w,h = cv2.boundingRect(c)
            if color == (255,0,0):
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x+w,y),(x,y+h),color,3)
                cv2.putText(frame,'Azul',(x+10,y+10),1,0.75,color,2,cv2.LINE_AA)
            if color == (0,255,255):
                M = cv2.moments(c)
                if (M['m00']==0): M['m00']=1
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
                xcentro = int(M['m10']/M['m00'])
                ycentro = int(M['m01']/M['m00'])
                radio = xcentro + x
                cv2.circle(frame,(xcentro,ycentro),radio,color,3)
                cv2.putText(frame,'Amarillo',(x+10,y-10),1,0.75,color,2,cv2.LINE_AA)

cap = cv2.VideoCapture(0)

azulBajo = np.array([100,100,20], np.uint8)
azulAlto = np.array([125,255,255], np.uint8)

amarilloBajo = np.array([15,100,20], np.uint8)
amarilloAlto = np.array([45,255,255], np.uint8)

fort = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read(0)

    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskAzul = cv2.inRange(frameHSV,azulBajo, azulAlto)
        maskAmarillo = cv2.inRange(frameHSV,amarilloBajo, amarilloAlto)
        dibujar(maskAzul,(255,0,0))
        dibujar(maskAmarillo,(0,255,255))
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()