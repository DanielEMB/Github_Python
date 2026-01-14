# 69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
# irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
# ordenados de menor a mayor.

cantidad = int(input("Introduce una cantidad exacta de números: "))
lista = []
numeroanterior = 0
for i in range(cantidad):
    numero = int(input("Introduce un número: "))
    lista.append(numero, )
lista.sort()
print(lista)