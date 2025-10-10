#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

letra = input("Introduce una letra")

if letra.isalpha():
    if letra.isupper() == True:
        print("La letra es mayúscula")
    elif letra.islower() == True:
        print("La letra es minúscula")
elif letra.isnumeric():
    print("Has introducido un número!!")
else:
    print("La letra es mayúscula ¿?")
