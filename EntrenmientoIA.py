import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 🔹 Datos reales (tamaño en m² y precio de casas en $)
X = np.array([50, 80, 100, 150, 200, 250, 300, 400, 500]).reshape(-1, 1)
y = np.array([150000, 240000, 300000, 450000, 600000, 750000, 900000, 1200000, 1500000])

# 🔹 Creamos el modelo de regresión
modelo = LinearRegression()

# 🔹 Guardaremos la pérdida en cada iteración
perdidas_historial = []

# 🔹 Entrenamos el modelo en múltiples iteraciones (simulación de epochs)
for epoca in range(1, 21):  # 20 épocas
    modelo.fit(X, y)  # Entrenamos el modelo con los datos
    y_pred = modelo.predict(X)  # Hacemos predicciones
    perdida = mean_squared_error(y, y_pred)  # Calculamos la pérdida (error cuadrático medio)

    perdidas_historial.append(perdida)  # Guardamos la pérdida
    print("Epoca: " + str(epoca) + ", Pérdida: " + str(perdida))  # Mostramos la pérdida

    # 🔹 Graficamos la pérdida en tiempo real
    plt.clf()
    plt.plot(perdidas_historial, marker="o", linestyle="-", color="blue", label="Pérdida")
    plt.xlabel("Época")
    plt.ylabel("Pérdida (Error cuadrático medio)")
    plt.title("Evolución de la Pérdida durante el Entrenamiento")
    plt.legend()
    plt.pause(0.3)  # Pequeña pausa para actualizar la gráfica

plt.show()  # Mostramos la gráfica final

print("✅ Entrenamiento finalizado.")
