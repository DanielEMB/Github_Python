# 65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayor y cuál el menor.
numero = 0
mayor = 0
menor  = 0
while numero != -99:
    numero = int(input("Introduce un número (-99 para terminar): "))
    if numero == -99:
        break
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")