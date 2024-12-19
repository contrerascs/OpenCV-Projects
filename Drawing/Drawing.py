import cv2
import numpy as np

imagen = 255*np.ones((400,600,3),dtype=np.uint8)

#Dibujando una linea
cv2.line(imagen,(0,0),(600,400),(255,0,0),3)

#Dibujando un rectangulo
cv2.rectangle(imagen,(50,80),(100,100),(0,255,0),1)

cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()