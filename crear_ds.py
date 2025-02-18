import cv2
import numpy as np
import os

# Ruta específica para guardar las imágenes
ruta_guardado = r'C:\Users\quiqu\OneDrive\Documents\uni\modular\dataset'  # Nota el prefijo "r" para evitar errores

# Crear la carpeta si no existe
if not os.path.exists(ruta_guardado):
    os.makedirs(ruta_guardado)

cap = cv2.VideoCapture(0)  # Usar la cámara (cambiar el índice si hay más cámaras)

i = 0
flash_duration = 10  # Duración del flash en frames
flash_counter = 0  # Contador para el efecto de flash

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Si está activo el flash, muestra un marco blanco
    if flash_counter > 0:
        flash_frame = np.full_like(frame, 255)  # Crear una imagen blanca
        cv2.imshow('Frame', flash_frame)
        flash_counter -= 1
    else:
        cv2.imshow('Frame', frame)

    # Presiona 'w' para guardar la imagen
    if cv2.waitKey(1) & 0xFF == ord('w'):
        # Guardar la imagen en la ruta especificada
        cv2.imwrite(f'{ruta_guardado}\\image_{i}.jpg', frame)
        i += 1
        flash_counter = flash_duration  # Activa el efecto de flash

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
