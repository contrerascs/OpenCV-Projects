import cv2
import numpy as np
import imutils

image = cv2.imread(r'Thresholding/img3.jpg',0)
image = imutils.resize(image, width=400)

_,binarizada = cv2.threshold(image,210,255,cv2.THRESH_BINARY)
_,binarizadaInv = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY_INV)
_,trunc = cv2.threshold(image,210,255,cv2.THRESH_TRUNC)
_,toZero = cv2.threshold(image,210,255,cv2.THRESH_TOZERO)
_,toZeroInv = cv2.threshold(image,210,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('Image',image)
cv2.imshow('Tipos: Binary - Binary Inv - Trunc - ToZero',np.hstack([binarizada, binarizadaInv, toZero, toZeroInv]))

cv2.waitKey(0)
cv2.destroyAllWindows()