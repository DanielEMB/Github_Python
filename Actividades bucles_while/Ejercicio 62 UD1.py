# 62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
# hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
numpares = ""
numimpares = ""
if num1 < num2:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            numpares += str(i) + "-"
        else:
            numimpares += str(i) + "-"
elif num1 > num2:
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            numpares += str(i) + "-"
        else:
            numimpares += str(i) + "-"
else:
    if num1 % 2 == 0:
        numpares = str(num1) + "-"
    else:
        numimpares = str(num1) + "-"
print("Los números pares son:", numpares[:-1])
print("Los números impares son:", numimpares[:-1])
