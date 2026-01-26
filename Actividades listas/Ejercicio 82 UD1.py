# 82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al
# azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine
# la palabra
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)
import random
numrandom = random.randint(0, 7)
correcto = ""  
while correcto != lista[numrandom]:
    correcto = input("Di la palabra escogida al azar: ")
    if correcto != lista[numrandom]:
        print("Has fallado, vuelve a intentarlo")
print("Has acertado!!, la palabra era: ", lista[numrandom])