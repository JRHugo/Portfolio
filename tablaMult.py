# Crea un juego donde el usuario tenga que adivinar un número aleatorio entre 1 y 10. 
# Usa while para repetir hasta que lo adivine.

import random

print ("Adivina el numero del 1 al 10")

while True:
    num = random.randint(1,10)
    adivina = int(input(""))
    if adivina == num:
        print ("Has adivinado el numero")
        break
    else:
        print("Sigue intentandolo")
        continue
print("Fin dle juego")



