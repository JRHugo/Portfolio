import tkinter as tk
from tkinter import filedialog, messagebox

import numpy as np
import tensorflow as tf
from PIL import Image, ImageTk

# Cargar el modelo preentrenado de TensorFlow (InceptionV3)
model = tf.keras.applications.InceptionV3(weights='imagenet')

# Función para cargar y procesar la imagen
def cargar_imagen():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((400, 400))  # Ajustar el tamaño para mostrar en la ventana
        img_tk = ImageTk.PhotoImage(img)
        label_imagen.config(image=img_tk)
        label_imagen.image = img_tk
        procesar_imagen(file_path)

# Función para procesar la imagen y generar la descripción
def procesar_imagen(file_path):
    # Leer la imagen con OpenCV
    img = cv2.imread(file_path)
    img = cv2.resize(img, (299, 299))  # Redimensionar a tamaño adecuado para InceptionV3
    img = tf.keras.applications.inception_v3.preprocess_input(img)  # Preprocesar la imagen

    # Predecir la imagen
    preds = model.predict(np.expand_dims(img, axis=0))
    decoded_preds = tf.keras.applications.inception_v3.decode_predictions(preds, top=3)[0]

    # Crear la descripción
    descripcion = "Descripción: "
    for i, (imagenet_id, label, score) in enumerate(decoded_preds):
        descripcion += f"{label} ({score*100:.2f}%), "

    descripcion = descripcion[:-2]  # Eliminar la última coma y espacio
    label_descripcion.config(text=descripcion)

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Imágenes a Texto")

# Estilo de la ventana
root.config(bg="#f0f0f0")

# Título
label_titulo = tk.Label(root, text="Conversor de Imágenes a Texto", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="black")
label_titulo.pack(pady=20)

# Botón para cargar la imagen
button_cargar = tk.Button(root, text="Cargar Imagen", font=("Arial", 14), bg="#4CAF50", fg="white", command=cargar_imagen)
button_cargar.pack(pady=10)

# Mostrar la imagen cargada
label_imagen = tk.Label(root, bg="#f0f0f0")
label_imagen.pack(pady=20)

# Mostrar la descripción generada
label_descripcion = tk.Label(root, text="Descripción: ", font=("Arial", 14), bg="#f0f0f0", fg="black")
label_descripcion.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
