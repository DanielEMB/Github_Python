lista = []
a = input()
lista = a.split()
b = ""
if len(lista) == 2:
    a = lista[0]
    b = lista[1]
if len(lista) == 1:
    b = input()
    lista.append(b)
lista.sort()

if a.islower() and b.islower():
    if a < b:
        print(a, "<", b)
    elif a > b:
        print(a, ">", b)
    elif a == b:
        print(a, "=", b)