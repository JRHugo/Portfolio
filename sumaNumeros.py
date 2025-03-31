# Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10 con un for

import math

num = int (input ("Introduce un numero: "))

for i in range(1,11):
    print (num, "*",i,"=", num * i)

