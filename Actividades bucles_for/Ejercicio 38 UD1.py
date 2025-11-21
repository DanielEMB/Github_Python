# 38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
# notas inferiores a 0 y superiores a 10

notas = int(input("Introduce el número de notas que deseas introducir"))

for i in range(1, notas):
    nota = float(input("Introduce tu nota"))
    if nota >= 0 and nota <= 10:
        if nota >= 5:
            print("Asignatura APROBADA")
        else:
            print("Asignatura SUSPENDIDA")
    else:
        print("Has itroducido una nota INCORRECTA")
