# 51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
# número de veces que desea que repita la frase Buenos días. Con While.
contador = 0
repeticiones = int(input("Introduce el número de veces para repetirse: "))
while contador < repeticiones:
    print("¡Buenos días!")
    contador += 1