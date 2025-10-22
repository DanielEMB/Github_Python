#27. Mejora el programa anterior para controlar que el valor introducido es una letra y
#en caso de introducir un número, aparezca un aviso por pantalla

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
