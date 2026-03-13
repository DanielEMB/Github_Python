lista = []
a = input()
b = 0
lista = a.split()
if len(lista) == 1:
    while len(lista) != 2:
        b = input()
        if b.isnumeric():
            a += " " + b
            lista = a.split()
        print(len(lista))
for i in range(len(lista)):
    if i == 0:
        a = int(lista[i])
    if i == 1:
        b = int(lista[i])
resultado = 0
residuo = 0
if b!= 0:
    resultado = a//b
    residuo = a % b 
    print(resultado, residuo)