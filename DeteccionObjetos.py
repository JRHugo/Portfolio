import cv2
import numpy as np
import torch
from ultralytics import YOLO
import matplotlib.pyplot as plt

# 1️⃣ Cargar el modelo YOLO preentrenado
modelo = YOLO("yolov8n.pt")  # 'yolov8n.pt' es un modelo liviano pero preciso

# 2️⃣ Cargar la imagen
imagen_path = "Agua.jpg"  # Reemplaza con tu imagen
imagen = cv2.imread(imagen_path)

# 3️⃣ Realizar la detección
resultados = modelo(imagen)

# 4️⃣ Dibujar los resultados en la imagen
for resultado in resultados:
    for box in resultado.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas del rectángulo
        etiqueta = modelo.names[int(box.cls[0])]  # Nombre del objeto detectado
        confianza = box.conf[0].item()  # Confianza de la detección

        # Dibujar rectángulo y texto en la imagen
        cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(imagen, f"{etiqueta} ({confianza:.2f})", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 5️⃣ Mostrar la imagen con detecciones
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen_rgb)
plt.axis("off")
plt.title("Detección de Objetos con YOLO")
plt.show()
