# 74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
# entre las 2 listas.

lista1 = ["casa","mesa","sal","sol","agua"]
lista2 = ["casa", "luz", "tres", "tren", "sol", "pan"]
listarepetidos = []
listanorepetidos = []

for i in lista2:
    if i in lista1:
        listarepetidos.append(i)
    else:
        listanorepetidos.append(i)
for i in lista1:
    if not i in lista2:
        listanorepetidos.append(i)
print("Están repetidas: ", listarepetidos)
print("No están repetidas: ", listanorepetidos)
