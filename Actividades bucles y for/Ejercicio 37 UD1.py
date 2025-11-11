# 37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

notas = int(input("Introduce el número de notas que deseas introducir"))

for i in range(1, notas):
    nota = int(input("Introduce tu nota"))
    if nota >= 5:
        print("Asignatura APROBADA")
    else:
        print("Asignatura SUSPENDIDA")
