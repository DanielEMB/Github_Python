# 26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

letra = input("Introduce una letra")

if letra.isalpha():
    if letra.isupper() == True:
        print("La letra es mayúscula")
    elif letra.islower() == True:
        print("La letra es minúscula")
else:
    print("La letra es mayúscula ¿?")
