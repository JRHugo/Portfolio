import cv2  
import matplotlib.pyplot as plt  

# 1️⃣ Cargar la imagen  
imagen = cv2.imread('Agua.jpg')   
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  

# 2️⃣ Convertir a escala de grises  
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  

# 3️⃣ Aplicar detección de bordes  
bordes = cv2.Canny(imagen_gris, 100, 200)  

# 4️⃣ Mostrar imágenes  
plt.figure(figsize=(10,5))  
plt.subplot(1,3,1), plt.imshow(imagen_rgb), plt.title('Imagen Original')  
plt.subplot(1,3,2), plt.imshow(imagen_gris, cmap='gray'), plt.title('Escala de Grises')  
plt.subplot(1,3,3), plt.imshow(bordes, cmap='gray'), plt.title('Detección de Bordes')  
plt.show()  
