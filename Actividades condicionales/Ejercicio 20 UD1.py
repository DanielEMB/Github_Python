#20. A partir del ejercicio anterior,
# forzar que el usuario solo pueda introducir por teclados números entre 0 y 10.

numero1 = float(input("Introduce el valor 1:"))
numero2 = float(input("Introduce el valor 2:"))
if numero1 <= 10 and numero1 >= 0 and numero2 <= 10 and numero2 >= 0:
    if numero1 > numero2:
        print(numero1, "Es mayor que", numero2)
    elif numero1 < numero2:
        print(numero2, "Es mayor que", numero1)
    else:
        print("Ambos son iguales")
else:
    print("Uno o los dos números están fuera de los límites establecidos")