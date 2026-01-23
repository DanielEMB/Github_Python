# 80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 

numero = input(("Inroduce un número que sea decimal o no: "))  
if numero.isalpha():
    print("Introduce un número")
elif float(numero) % 1!= 0:
    print("El número es decimal")
else:
    print("El número no es decimal")