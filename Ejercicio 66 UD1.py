# 66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
# se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 
import random
import time
contador = 0
inicio = time.time()
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0
while time.time() - inicio < 3:
    dado = random.randint(1, 6)
    contador += 1
    if dado == 1:
        uno += 1    
    elif dado == 2:
        dos += 1
    elif dado == 3:
        tres += 1
    elif dado == 4:
        cuatro += 1
    elif dado == 5:
        cinco += 1
    else:
        seis += 1
print("El número 1 ha salido", uno, "veces.")
print("El número 2 ha salido", dos, "veces.")
print("El número 3 ha salido", tres, "veces.")
print("El número 4 ha salido", cuatro, "veces.")
print("El número 5 ha salido", cinco, "veces.")
print("El número 6 ha salido", seis, "veces.")