import cv2

imagen = cv2.imread(r'Read Image/Gojo.jpg',0)
cv2.imshow('Prueba de imagen', imagen)
cv2.imwrite(r'Read Image/Grises.jpg',imagen)
cv2.waitKey(5000)
cv2.destroyAllWindows()