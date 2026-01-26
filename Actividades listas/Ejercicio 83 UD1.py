# 83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta
# que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente
# manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así
# sucesivamente.
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)
import random
correcto = ""
errores = 0
puntostotal = 0
partidas = int(input("Introduce el número de partidas que quieres jugar: "))  
while partidas > 0:
    numrandom = random.randint(0, 7)
    while correcto != lista[numrandom]:
        correcto = input("Di la palabra escogida al azar: ")
        if correcto != lista[numrandom]:
            print("Has fallado, vuelve a intentarlo")
            errores += 1
    puntos = 8 - errores
    puntostotal += puntos
    errores = 0
    print("Has conseguido", puntos, "puntos en esta partida.")
    print("Has acertado!!, la palabra era: ", lista[numrandom])
    partidas -= 1
    if partidas > 1:
        print("SIGUIENTE PARTIDA...")
    print(lista)
print("Has conseguido un total de: ", puntostotal + puntos, "puntos en todas las partidas.")