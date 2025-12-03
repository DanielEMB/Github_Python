# 58. 58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random

numaleatorio = random.randint(1, 5)
final = 0
numintroducido = int(input("Introduce un número del 1 al 5: "))
contador = 0
while not numaleatorio == numintroducido:
    contador +=1
    if contador == 3:
        break
    if numintroducido >= 1 or numintroducido <=5:
        print("No has acertado")
        numintroducido = int(input("Introduce un número del 1 al 5: "))
    else:
        numintroducido = int(input("No has introducido un número del 1 al 5. Introduce un número del 1 al 5: "))
if numaleatorio == numintroducido:
    print("Has acertado")