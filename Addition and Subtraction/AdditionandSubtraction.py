import cv2

img1 = cv2.imread(r'Addition and Subtraction/Imagen1.jpg',0)
img2 = cv2.imread(r'Addition and Subtraction/Imagen2.jpg',0)
resA = cv2.add(img1,img2)

#Transparencia de las imagen
#resAW = cv2.addWeighted(img1,0.5,img2,0.5,0)
#cv2.imshow('resAW',resAW)

#sustracción
resultado = cv2.subtract(img1,img2)
resultado2 = cv2.absdiff(img1,img2)

cv2.imshow('Resultado 1',resultado)
cv2.imshow('Resultado 2',resultado2)


#cv2.imshow('resA',resA)

#cv2.imshow('img1',img1)
#cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()