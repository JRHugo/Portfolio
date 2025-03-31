import time
import numpy as np
import matplotlib.pyplot as plt


# Simulación de entrenamiento de un modelo de IA
epocas = 50
perdida = 1.0  # Pérdida inicial
perdidas = []  # Lista para almacenar la pérdida en cada época


for epoca in range(1, epocas + 1):
    reduccion= np.random.uniform(0.05, 0.15)  # Simulamos una reducción de pérdida
    perdida -= perdida * reduccion
    perdidas.append(perdida)

    print("Epoca:"+ str(epoca) + " - Pérdida: " + str(perdida))
        
    if epoca % 10 == 0:
        print("Checkpoint guardado")
        time.sleep(0.2)

print ("Entrenamiento finalizado")

# Gráfica de pérdida
plt.figure(figsize=(8,5))
plt.plot(range(1, epocas+1), perdidas, marker="o", linestyle="-", color="red")
plt.xlabel("Épocas")
plt.ylabel("Pérdida")
plt.title("Evolución de la Pérdida durante el Entrenamiento")
plt.show()
