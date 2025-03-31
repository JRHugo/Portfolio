import tkinter as tk
import secrets
import string
import pyperclip
from tkinter import messagebox

def generar_contraseña():
    # Obtener la longitud de la contraseña desde la entrada
    longitud = int(entry_longitud.get())

    # Conjuntos de caracteres para la contraseña
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Generar la contraseña usando secrets para mayor seguridad
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))

    # Mostrar la contraseña generada en el label
    label_resultado.config(text=f"Contraseña Generada: {contraseña}")

    # Evaluar la seguridad de la contraseña
    seguridad = evaluar_seguridad(contraseña)
    label_seguridad.config(text=f"Seguridad: {seguridad[0]}", fg=seguridad[1])

    # Copiar la contraseña al portapapeles
    pyperclip.copy(contraseña)

    # Mostrar un mensaje recomendando el uso de un gestor de contraseñas
    messagebox.showinfo("Consejo", "¡Contraseña copiada al portapapeles! Usa un gestor de contraseñas para guardarla de forma segura.")

def evaluar_seguridad(contraseña):
    # Función para evaluar la fuerza de la contraseña
    if len(contraseña) < 8:
        return ("Débil", "red")
    elif len(contraseña) < 12:
        return ("Media", "orange")
    else:
        return ("Fuerte", "green")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas Seguras")

# Estilo de la ventana
root.config(bg="#f0f0f0")

# Título
label_titulo = tk.Label(root, text="Generador de Contraseñas Seguras", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="black")
label_titulo.pack(pady=20)

# Longitud de la contraseña
label_longitud = tk.Label(root, text="Longitud de la Contraseña:", bg="#f0f0f0", fg="black")
label_longitud.pack()
entry_longitud = tk.Entry(root, font=("Arial", 14), width=10)
entry_longitud.pack(pady=5)
entry_longitud.insert(0, "16")  # Longitud predeterminada

# Botón para generar la contraseña
button_generar = tk.Button(root, text="Generar Contraseña", font=("Arial", 14), bg="#4CAF50", fg="white", command=generar_contraseña)
button_generar.pack(pady=20)

# Mostrar la contraseña generada
label_resultado = tk.Label(root, text="Contraseña Generada: ", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="black")
label_resultado.pack(pady=10)

# Seguridad de la contraseña
label_seguridad = tk.Label(root, text="Seguridad: ", font=("Arial", 12), bg="#f0f0f0", fg="black")
label_seguridad.pack(pady=5)

# Consejos adicionales
label_consejos = tk.Label(root, text="¡Recuerda usar un gestor de contraseñas!", font=("Arial", 10, "italic"), bg="#f0f0f0", fg="gray")
label_consejos.pack(pady=5)

# Iniciar la aplicación
root.mainloop()

