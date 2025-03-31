import tkinter as tk
import string
import re
from tkinter import messagebox

def evaluar_contraseña():
    # Obtener la contraseña del usuario
    contraseña = entry_contraseña.get()

    # Evaluar la fortaleza de la contraseña
    seguridad, color = evaluar_seguridad(contraseña)

    # Mostrar la evaluación en la interfaz
    label_seguridad.config(text=f"Seguridad: {seguridad}", fg=color)

    # Dar recomendaciones para mejorar la contraseña
    recomendaciones = obtener_recomendaciones(contraseña)
    label_recomendaciones.config(text=recomendaciones)

def evaluar_seguridad(contraseña):
    # Evaluación basada en la longitud y complejidad de la contraseña
    longitud = len(contraseña)
    tiene_mayusculas = bool(re.search(r'[A-Z]', contraseña))
    tiene_minusculas = bool(re.search(r'[a-z]', contraseña))
    tiene_numeros = bool(re.search(r'[0-9]', contraseña))
    tiene_simbolos = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña))

    # Reglas de seguridad
    if longitud < 8:
        return "Débil", "red"
    elif longitud < 12:
        return "Media", "orange"
    elif longitud >= 12 and tiene_mayusculas and tiene_minusculas and tiene_numeros and tiene_simbolos:
        return "Fuerte", "green"
    else:
        return "Media", "orange"

def obtener_recomendaciones(contraseña):
    recomendaciones = []

    # Verificar las debilidades de la contraseña y recomendar lo que falta
    if len(contraseña) < 8:
        recomendaciones.append("- La contraseña es demasiado corta. Se recomienda al menos 8 caracteres.")
    
    if not re.search(r'[A-Z]', contraseña):
        recomendaciones.append("- Usa al menos una letra mayúscula.")
    
    if not re.search(r'[a-z]', contraseña):
        recomendaciones.append("- Usa al menos una letra minúscula.")
    
    if not re.search(r'[0-9]', contraseña):
        recomendaciones.append("- Usa al menos un número.")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        recomendaciones.append("- Usa al menos un símbolo especial (!@#$%^&*...).")
    
    # Si la contraseña es segura, se le felicita
    if len(recomendaciones) == 0:
        recomendaciones.append("¡Tu contraseña es segura! Pero aún puedes mejorarla agregando más complejidad.")

    # Combinar todas las recomendaciones en un solo texto
    return "\n".join(recomendaciones)

# Crear la ventana principal
root = tk.Tk()
root.title("Verificador de Seguridad de Contraseñas")

# Estilo de la ventana
root.config(bg="#f0f0f0")

# Título
label_titulo = tk.Label(root, text="Verificador de Seguridad de Contraseñas", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="black")
label_titulo.pack(pady=20)

# Ingreso de la contraseña
label_contraseña = tk.Label(root, text="Ingresa tu Contraseña:", bg="#f0f0f0", fg="black")
label_contraseña.pack()
entry_contraseña = tk.Entry(root, font=("Arial", 14), show="*", width=20)
entry_contraseña.pack(pady=5)

# Botón para evaluar la contraseña
button_evaluar = tk.Button(root, text="Evaluar Contraseña", font=("Arial", 14), bg="#4CAF50", fg="white", command=evaluar_contraseña)
button_evaluar.pack(pady=20)

# Mostrar el resultado de la seguridad
label_seguridad = tk.Label(root, text="Seguridad: ", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="black")
label_seguridad.pack(pady=10)

# Mostrar las recomendaciones para mejorar la contraseña
label_recomendaciones = tk.Label(root, text="Recomendaciones:", font=("Arial", 12), bg="#f0f0f0", fg="black")
label_recomendaciones.pack(pady=10)

# Iniciar la aplicación
root.mainloop()

