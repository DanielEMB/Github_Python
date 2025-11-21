# 52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
# pantalla. El programa preguntará si deseas o no repetir la operación. Con While
repetir = ""
while repetir == "s" or repetir == "":
    numero1 = int(input("Introduce el 1er número: "))
    numero2 = int(input("Introduce el 2ndo número: "))
    suma = numero1 + numero2
    print("El resultado de la suma es: ", suma)
    repetir = input("deseas repetir la operación? s/n: ")
print("Programa finalizado")
