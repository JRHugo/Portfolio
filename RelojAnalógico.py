import tkinter as tk
import time
import math

def actualizar_reloj():
    hora_actual = time.localtime()
    segundos = hora_actual.tm_sec
    minutos = hora_actual.tm_min
    horas = hora_actual.tm_hour

    # Limpia el lienzo
    lienzo.delete("all")

    # Dibuja el reloj
    lienzo.create_oval(10, 10, 200, 200, outline="black", width=2)

    # Dibuja las agujas
    lienzo.create_line(100, 100, 100 + 40 * math.cos(math.radians((horas % 12) * 30 - 90)),
                       100 + 40 * math.sin(math.radians((horas % 12) * 30 - 90)), width=4, fill="black")
    lienzo.create_line(100, 100, 100 + 50 * math.cos(math.radians(minutos * 6 - 90)),
                       100 + 50 * math.sin(math.radians(minutos * 6 - 90)), width=3, fill="blue")
    lienzo.create_line(100, 100, 100 + 60 * math.cos(math.radians(segundos * 6 - 90)),
                       100 + 60 * math.sin(math.radians(segundos * 6 - 90)), width=2, fill="red")

    # Actualiza el reloj cada segundo
    root.after(1000, actualizar_reloj)

# Configuración de la ventana
root = tk.Tk()
root.title("Reloj Analógico")
lienzo = tk.Canvas(root, width=200, height=200)
lienzo.pack()

actualizar_reloj()

root.mainloop()
