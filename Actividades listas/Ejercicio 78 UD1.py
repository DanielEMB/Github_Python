# 78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
# eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir.

lista1 = ["a","b","D","x","r","X","3","h","w","2","i"]
respuesta = "s"
print(lista1)
while respuesta == "s":
    numero = input("Que número deseas eliminar?: ")
    if numero.isnumeric():
        print()
    else:
        print("Introduce un valor numérico")
    if numero in lista1:
        lista1.remove(numero)
    respuesta = input("Deseas introducir otro valor s/n?: ")
print(lista1)