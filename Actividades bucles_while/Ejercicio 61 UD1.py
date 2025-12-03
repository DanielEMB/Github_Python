# 61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
# superior o igual a 40.

num = int(input("Introduce un número para mostrar su tabla del 1 al 10: "))
nummultiplicado = num
while nummultiplicado != num * 11 and nummultiplicado <= 40:
    print(nummultiplicado)
    nummultiplicado = nummultiplicado + num