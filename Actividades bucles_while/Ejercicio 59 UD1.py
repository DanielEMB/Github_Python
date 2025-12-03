# 59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
# intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
# menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
# mostrarse por pantalla un mensaje y el número de intentos.

import random
numal = random.randint(0, 1000)
num = -1
while num != numal:
    num = int(input("Introduce un número del 1 al 1000: "))
    if num > numal:
        print("El número random es menor")
    elif num < numal:
        print("El número introducido es mayor")
    else:
        print("¡Has acertado!")