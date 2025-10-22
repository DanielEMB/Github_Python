#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido.
#  Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

nota = float(input("Introduce la nota que has sacado"))

if nota <= 10 and nota >= 0:
    if nota >= 5:
        print("Has aprobado!!!")
    else:
        print("Has suspendido...")
else:
    print("La nota que has introducido no está entre 0 y 10.")
