# 76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
# y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
# en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.

lista1 = ["a","b","D","x","r","X","3","h","w","2","i"]
orden = int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
listanumeros = []
listaletras = []
letrasmayusculas = []
for i in lista1:
    if i.isnumeric():
        listanumeros.append(i)
    if i.isalpha():
        listaletras.append(i)
        if i.isupper():
            letrasmayusculas.append(i)
listaletras.sort()
listanumeros.sort()
letrasmayusculas.sort()
for i in letrasmayusculas:
    listanumeros.insert()
if orden == 1:
    print(listanumeros)
    print(listaletras)