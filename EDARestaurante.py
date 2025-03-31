import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset de Kaggle (Ejemplo: Predicción de precios de casas)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Mostrar primeras filas
print(df.head())

# Histograma de los precios de las casas
plt.figure(figsize=(8,5))
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.xlabel("Cuenta total ($)")
plt.ylabel("Frecuencia")
plt.title("Distribución de las cuentas en el restaurante")
plt.show()

# Mapa de calor para ver correlaciones
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Calor de Correlaciones")
plt.show()
