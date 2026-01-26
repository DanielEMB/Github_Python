# 84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las
# palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la
# palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)
import random
numrandom = random.randint(0, 7)
letras = list(lista[numrandom])
letrasdes = random.shuffle(letras)
palabradesordenada = ''.join(letras)
print("La palabra desordenada es:", palabradesordenada)
correcto = letras
while letras != lista[numrandom]:
    letras = input("Di la palabra escogida al azar: ")
    if letras != lista[numrandom]:
        print("Has fallado, vuelve a intentarlo")
print("Has acertado!!, la palabra era: ", lista[numrandom])