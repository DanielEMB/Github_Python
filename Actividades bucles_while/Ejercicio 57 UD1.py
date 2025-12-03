# 57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
# debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random

numaleatorio = random.randint(1, 5)
final = 0
numintroducido = int(input("Introduce un número del 1 al 5: "))
while numaleatorio != numintroducido:
    if numintroducido >= 1 or numintroducido <=5:
        print("No has acertado")
        numintroducido = int(input("Introduce un número del 1 al 5: "))
    else:
        print("No has introducido un número del 1 al 5.")
print("Has acertado")