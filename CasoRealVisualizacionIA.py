import time
import random
import matplotlib.pyplot as plt

# Inicializamos variables
perdida = 1.0
epoca = 1
max_epocas = 50
perdidas_historial = []  # Lista para almacenar la pérdida de cada época
perdida_anterior = perdida
aumentos_consecutivos = 0  # Contador para detectar aumentos seguidos

plt.ion()  # Activamos el modo interactivo para visualizar en tiempo real

while perdida > 0.1 and epoca <= max_epocas:
    print("Epoca: " + str(epoca) + " - Pérdida: " + str(perdida))   
    # Guardamos la pérdida en el historial
    perdidas_historial.append(perdida)
    
    # Reducimos la pérdida en un porcentaje aleatorio entre 5% y 15%
    nueva_perdida = perdida - (perdida * random.uniform(0.05, 0.15))

    # TODO: Detectar si la pérdida aumenta en dos épocas consecutivas
    if nueva_perdida > perdida:
        aumentos_consecutivos += 1
        if aumentos_consecutivos == 2:
            print("🚨 ¡La pérdida aumentó dos veces seguidas! Deteniendo entrenamiento...")
            break
    else:
        aumentos_consecutivos = 0  # Reiniciamos el contador si no hay aumento

    perdida = nueva_perdida  # Actualizamos la pérdida
    epoca += 1  # Pasamos a la siguiente época

    if epoca % 10 == 0:
        print("💾 Checkpoint guardado.")

    # TODO: Generar y actualizar la gráfica en tiempo real
    plt.clf()  # Limpiar gráfico anterior
    plt.plot(perdidas_historial, label="Pérdida")
    plt.xlabel("Época")
    plt.ylabel("Pérdida")
    plt.title("Monitoreo de Pérdida en Entrenamiento")
    plt.legend()
    plt.pause(0.1)  # Pequeña pausa para actualizar la gráfica

    time.sleep(0.3)  # Simula tiempo de procesamiento

plt.ioff()  # Desactivamos el modo interactivo
plt.show()  # Mostramos el gráfico final

if perdida <= 0.1:
    print("✅ Entrenamiento finalizado. Pérdida aceptable alcanzada.")
else:
    print("❌ Entrenamiento detenido.")
