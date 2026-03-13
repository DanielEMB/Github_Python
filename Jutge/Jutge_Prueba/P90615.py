listanumeros = []
numeros = input()
listanumeros = numeros.split()
for i in range(len(listanumeros)):
    listanumeros[i] = int(listanumeros[i])
numeromax = max(listanumeros)
print(numeromax)