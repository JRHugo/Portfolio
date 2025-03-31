# Crea un juego donde el usuario tenga que adivinar una palabra aleatoria, donde el programa le dirá la posición de la letra es correcta o no. 
# Usa while para repetir hasta que lo adivine.

import random

print("Adivina la palabra secreta")

palabras = ["casa", "perro", "gato", "pajaro", "pescado", "tortuga", "leon", "elefante", "jirafa", "cocodrilo", "serpiente", "tigre", "oso", "conejo", "raton", "murcielago", "ballena", "delfin", "tiburon", "pulpo", "medusa", "caballo", "vaca", "cerdo", "oveja", "gallo", "pato", "aguila", "halcon", "loro", "pajaro", "abeja", "mariposa", "mosca", "araña", "escorpion", "cienpies", "caracol", "hormiga", "saltamontes", "grillo", "libelula", "alacran", "ciempies", "araña", "escarabajo", "mariposa", "abeja", "mosca", "avispa", "cucaracha", "chinche", "pulga", "garrapata", "mosquito", "polilla", "hormiga", "saltamontes", "grillo", "libelula", "alacran", "ciempies", "araña", "escarabajo", "mariposa", "abeja", "mosca", "avispa", "cucaracha", "chinche", "pulga", "garra"]

# Selecciona una palabra aleatoria antes de entrar en el bucle
palabra = random.choice(palabras)
print("La palabra tiene", len(palabra), "letras")

while True:
    Adivina = input("Ingrese su palabra: ")
    if Adivina == palabra:
        print("Felicidades, adivinaste la palabra")
        break
    else:
        for i in range(len(palabra)):
            if i < len(Adivina) and Adivina[i] == palabra[i]:
                print(f"La letra '{Adivina[i]}' está en la posición correcta ({i+1})")
            elif i < len(Adivina) and Adivina[i] in palabra:
                print(f"La letra '{Adivina[i]}' está en la palabra pero no en la posición correcta")
        print("Intenta de nuevo")