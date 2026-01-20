# 72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
# no deben almacenarse en la lista
lista = []

repetir = ""
while not repetir == "n":
    letra = input("Introduce una letra: ")
    if letra.isalpha():
        lista.append(letra)
        repetir = input("Deseas repetir? s/n: ")
lista = set(lista)
print(lista)
#EJERCICIO NO ACABDO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!