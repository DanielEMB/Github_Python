# 60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
# Utiliza únicamente el while

num = int(input("Introduce un número para mostrar su tabla del 1 al 10"))
nummultiplicado = num
while nummultiplicado != num * 11:
    print(nummultiplicado)
    nummultiplicado = nummultiplicado + num