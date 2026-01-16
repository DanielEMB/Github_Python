# 71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
# esta lista no deben almacenarse las letras que se han introducido repetidas.
lista = []
repetir = ""
while not repetir == "n":
    letra = input("Introduce una letra: ")
    if letra.isalpha():
        lista.append(letra)
        repetir = input("Deseas repetir? s/n: ")
lista = set(lista)
print(lista)