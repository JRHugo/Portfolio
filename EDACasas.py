import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset de Kaggle (Ejemplo: Predicción de precios de casas)
df = pd.read_csv("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv")

# Mostrar primeras filas
print(df.head())

# Crear un gráfico de dispersión
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["total_rooms"], y=df["median_house_value"], alpha=0.5)

# Etiquetas
plt.xlabel("Número total de habitaciones")
plt.ylabel("Precio medio de la casa ($)")
plt.title("Relación entre tamaño de casa y precio")

plt.show()

# Gráfico de dispersión con línea de regresión
plt.figure(figsize=(8,5))
sns.regplot(x=df["total_rooms"], y=df["median_house_value"], scatter_kws={"alpha":0.3}, line_kws={"color":"red"})

# Etiquetas
plt.xlabel("Número total de habitaciones")
plt.ylabel("Precio medio de la casa ($)")
plt.title("Tendencia entre tamaño de casa y precio")

plt.show()