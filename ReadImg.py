import cv2

imagen = cv2.imread('Gojo.jpg')
cv2.imshow('Prueba de imagen', imagen)
cv2.waitKey(5000)
cv2.destroyAllWindows()