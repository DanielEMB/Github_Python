#35. Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre.

nombre = input("Introduce tu nombre")
numero = int(input("Introduce un número"))

for i in range(1, numero):
    print(nombre)
