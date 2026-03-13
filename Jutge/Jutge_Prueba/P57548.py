numeros = input()
listanumeros = []
listanumeros = numeros.split(" ")
if len(numeros) == 1:
    numero = input()
    listanumeros.append(numero)
for i in range(0, len(listanumeros)):
    listanumeros[i] = int(listanumeros[i])
suma = sum((listanumeros))
print(suma)