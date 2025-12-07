# 64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
# -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
# a) total de pares
# b) total de impares
# c) total de números positivos
# d) total de números negativos
# e) total de ceros
# f) total de la suma de todos los números introducidos
numero = 0
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
suma_total = 0

while numero != -99:
    numero = int(input("introduce un número (-99 para terminar): "))
    if numero == -99:
        break
    if numero %2 == 0:
        pares += 1
    else:
        impares += 1    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1 
    else:
        ceros += 1
    suma_total += numero
print(f"Números pares: {pares}")
print(f"Números impares: {impares}") 
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números ceros: {ceros}")
print(f"Suma total de los números introducidos: {suma_total}")
