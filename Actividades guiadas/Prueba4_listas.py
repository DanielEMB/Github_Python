listanumeros = []
listanonumeros = []
listatodo = []

frase = input("Introduce valores separados por un guión:")
listatodo = frase.split("-")
for x in listatodo:
    print(x)
    if x.isnumeric():
        listanumeros.append(int(x))
    else:
        listanonumeros.append(x)
#for x in range(len(listatodo)):
#    if listatodo[x].isnumeric():
#        listanumeros.append(int(listatodo[x]))
#    else:
#        listanonumeros.append(listatodo[x])
print(listanumeros)

print(sum(listanumeros))