var1 = "laptop:800:5-raton:25:10-teclado:50:0-monitor:200:3-raton:25:10"
lista1 = var1.split("-")
lista_producto = []
lista_precio = []
lista_stock = []

for x in lista1:
    lista2 = var1.split(":")
    lista_producto.append(lista2[0])
    lista_precio.append(lista2[1])
    lista_stock.append(lista2[2])
lista_precio = [int(x) for x in lista_precio]
lista_stock = [int(x) for x in lista_stock]
for j in range(len(lista_precio)):
    precio_total += (lista_precio[j] * lista_stock[j]) 
print(precio_total)
mascaro = max(lista_precio)
posicion = lista_precio.index(mascaro)
print("el producto con stock a cero es", lista_producto[])
#acabar enunciado