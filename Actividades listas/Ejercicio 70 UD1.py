# 70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
# introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
# pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
# formato de entrada y salida tal y como se muestra en el testeo.
lista1 = []

cantidad = int(input("Introduce la cantidad de palabras: "))
for i in range(cantidad):
    palabra = input("Introduce una palabra: ")
    lista1.append(palabra)
lista1.sort()
lista2 = lista1
lista2.reverse()
print(lista1)
print(lista2)