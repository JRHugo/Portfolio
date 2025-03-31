# Ejercicio machine learning
import time
import random


modelos = input ("Introduce el número de modelos a entrenar: ")
modelos = int(modelos)
resultados = []

for modelo in range (modelos):
    print("Entrenando modelo " + str(modelo + 1) + "...")

    perdida = 1.0  # Pérdida inicial
    epoca = 1  # Contador de épocas
    max_epocas = 30  # Número máximo de épocas
    perdida_anterior = perdida # Pérdida anterior

    while perdida > 0.1 and epoca < max_epocas:  # ❓ Completa la condición aquí
        print( "Epoca: " + str(epoca) + " Pérdida: " + str(perdida))
        
        # Reducimos la pérdida en un porcentaje aleatorio entre 5% y 15%
        perdida -= perdida * random.uniform(0.05, 0.15)

        if perdida > perdida_anterior:
            print("La pérdida aumentó. Deteniendo entrenamiento.")
            break  
        perdida_anterior = perdida

        epoca += 1  # Aumentamos la cuenta de épocas
        if epoca % 10 == 0:
            print("Checkpoint del modelo guardado.")
        time.sleep(0.1)  # Simula tiempo de procesamiento

    if perdida < 0.1:
        print("✅ Entrenamiento finalizado. Pérdida aceptable alcanzada.")
    else: 
        print("❌ Entrenamiento finalizado. Pérdida máxima alcanzada.")

    resultados.append((modelo, epoca, perdida))
print("Resultados del entrenamiento:")
for modelo, epoca, perdida in resultados:
    print("Modelo " + str(modelo + 1) + " - Epocas: " + str(epoca) + ", Pérdida final: " + str(perdida))    

    