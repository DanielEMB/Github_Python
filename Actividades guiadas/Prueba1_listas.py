lista=[1,2,3,4,5,6]
lista2=[]
maximo=max(lista)
minimo=min(lista)
suma=sum(lista)
print(lista)
print("numero maximo", maximo)
print("numero minimo", minimo)
print("Suma total", suma)
for i in range (len(lista)):
    calculo=lista[i] * 2
    lista2.append(calculo)
print(lista2)
lista2=[]
for i in lista:
    lista2.append(i*2)
print(lista2)
lista2=[n*2 for n in lista]
print(lista2)