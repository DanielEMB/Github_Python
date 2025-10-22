#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

numero1 = float(input("Introduce el valor 1:"))
numero2 = float(input("Introduce el valor 2:"))

if numero1 > numero2:
    print(numero1, "Es mayor que", numero2)
elif numero1 < numero2:
    print(numero2, "Es mayor que", numero1)
else:
    print("Ambos son iguales")