# 41. Imprime el siguiente patrón utilizando for:
numero = "5"
for i in range(4, 0, -1):
    numero = numero + str(i)

for i in range(0, 5):
    print(numero)
    numero = numero[1:]