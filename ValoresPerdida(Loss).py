import matplotlib.pyplot as plt
import numpy as np

# Simulamos los valores de pérdida en 50 épocas
epocas = list(range(1, 51))
perdida = [np.exp(-e/10) + np.random.uniform(-0.05, 0.05) for e in epocas]  # Generamos valores con ruido

# Graficamos
plt.plot(epocas, perdida, marker='o', linestyle='-', color='b', label="Pérdida")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.title("Evolución de la pérdida en el entrenamiento")
plt.legend()
plt.grid()
plt.show()
