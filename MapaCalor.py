import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Clases del modelo (ejemplo: 3 categorías)
clases = ["Gato", "Perro", "Pájaro"]

# Creamos una matriz de confusión ficticia
matriz_confusion = np.zeros((3, 3))

# Llenamos la matriz con valores aleatorios (pero más altos en la diagonal para simular buen desempeño)
for i in range(3):
    for j in range(3):
        matriz_confusion[i][j] = np.random.randint(5, 50) if i != j else np.random.randint(50, 100)

# Convertimos a DataFrame para mejor visualización
df_matriz = pd.DataFrame(matriz_confusion, index=clases, columns=clases)

# Visualización con mapa de calor
plt.figure(figsize=(6,5))
sns.heatmap(df_matriz, annot=True, cmap="Blues", fmt=".0f")
plt.xlabel("Predicción")
plt.ylabel("Valor real")
plt.title("Matriz de Confusión")
plt.show()
