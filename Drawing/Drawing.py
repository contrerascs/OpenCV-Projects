import cv2
import numpy as np

imagen = 255*np.ones((400,600,3),dtype=np.uint8)

#Dibujando una linea
cv2.line(imagen,(0,0),(600,400),(255,0,0),3)

#Dibujando un rectangulo
cv2.rectangle(imagen,(50,80),(150,150),(0,255,0),1)

#Dibujando un circulo
cv2.circle(imagen,(300,200),100,(255,255,0),-1)

#Agregar texto
#font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(imagen, 'Practicando con OpenCV',(10,30),font,1,(0,255,255),2,cv2.LINE_AA)

#Tambien podemos asignar la fuente con numero, lo cuales vienen por defecto en OpenCV
cv2.putText(imagen,'Practicando con OpenCV', (10,20),0,1,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV', (10,60),1,1,(0,0,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV', (10,90),2,1,(0,255,0),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV', (10,120),3,1,(255,0,255),2,cv2.LINE_AA)
cv2.putText(imagen,'Practicando con OpenCV', (10,150),7,1,(155,100,155),2,cv2.LINE_AA)

cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()