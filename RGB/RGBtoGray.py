import cv2
import numpy as np

bgr = cv2.imread(r'RGB/prueba.png')

gris = cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)

cv2.imshow('GRISES',gris)
cv2.waitKey(0)
cv2.destroyAllWindows()