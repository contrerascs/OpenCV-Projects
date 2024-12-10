import cv2

captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter('VideoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while(captura.isOpened()):
    ret,imagen = captura.read()
    if ret == True:
        salida.write(imagen)
        cv2.imshow('video',imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
captura.release()
salida.release()
cv2.destroyAllWindows()