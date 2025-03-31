import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1️⃣ Generar datos simulados
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, n_classes=2, n_clusters_per_class=1, random_state=42)

# 2️⃣ Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3️⃣ Entrenar el modelo de clasificación
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# 4️⃣ Crear una visualización de la frontera de decisión
plt.figure(figsize=(8, 5))

# Crear una malla de puntos para graficar la frontera de decisión
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

# Predecir las clases para cada punto de la malla
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Dibujar la frontera de decisión
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdBu)

# Graficar los puntos de entrenamiento
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.RdBu, edgecolors='k', label="Entrenamiento")

# Graficar los puntos de prueba
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.RdBu, edgecolors='k', marker="*", s=100, label="Prueba")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Clasificación con Regresión Logística")
plt.legend()
plt.show()
