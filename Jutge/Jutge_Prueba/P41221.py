numeros = input()
listanumeros = []
listanumeros = numeros.split()

if len(listanumeros) == 0: # SI HAS INTRODUCIDO 0 NÚMEROS
    while len(listanumeros) != 3: # INTRODUCE CARACTERES HASTA QUE SEAN 3 NUMEROS
        numero = input()
        if numero.isnumeric(): #(POR SI INPUTEAS ALGO QUE NO ES NUMERO)
            numeros+= " " + numero
            listanumeros = numeros.split()
if len(listanumeros) == 1: # SI HAS INTRODUCIDO 1 NÚMEROS
    while len(listanumeros) != 3: # INTRODUCE NUMEROS HASTA QUE SEAN 3.
        numero = input()
        if numero.isnumeric():
            numeros+= " " + numero
            listanumeros = numeros.split()
if len(listanumeros) == 2: # SI HAS INTRODUCIDO 2 NÚMEROS
    while len(listanumeros) != 3: # INTRODUCE UN NUMERO HASTA QUE HAYAN 3.
        numero = input()
        if numero.isnumeric(): 
            numeros+= " " + numero
            listanumeros = numeros.split()

for i in range (0, len(listanumeros)):
    listanumeros[i] = int(listanumeros[i])
suma = sum((listanumeros))
print(suma)