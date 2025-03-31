# Ejercicio machine learning
import time
import random

perdida = 1.0  # Pérdida inicial
epoca = 1  # Contador de épocas
max_epocas = 10  # Número máximo de épocas

while perdida > 0.1 and epoca < max_epocas:  # ❓ Completa la condición aquí
    print(f"Época {epoca}: Pérdida actual = {perdida:.4f}")
    
    # Reducimos la pérdida en un porcentaje aleatorio entre 5% y 15%
    perdida -= perdida * random.uniform(0.05, 0.15)  

    epoca += 1  # Aumentamos la cuenta de épocas
    time.sleep(0.3)  # Simula tiempo de procesamiento


if perdida < 0.1:
    print("✅ Entrenamiento finalizado. Pérdida aceptable alcanzada.")
else: 
    print("❌ Entrenamiento finalizado. Pérdida máxima alcanzada.")