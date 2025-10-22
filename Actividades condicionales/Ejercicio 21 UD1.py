# 21. Programa que calcula una ecuación de segundo grado.
# Controla que el valor de la raíz cuadrada no de un valor negativo
import math

valor_ax2 = float(input("Introduce el valor ax elevado ^ 2"))
valor_bx = float(input("Introduce el valor bx"))
valor_c = float(input("Introduce c"))

discriminante = valor_bx ** 2 - (4 * valor_ax2 * valor_c)

if discriminante > 0:
    #ecuación:
    x1 = (-valor_bx + math.sqrt(discriminante)) / 2 * valor_ax2
    x2 = (-valor_bx - math.sqrt(discriminante)) / 2 * valor_ax2
    print("El valor de x1 es:", x1)
    print("El valor de x2 es:", x2)
else:   
    print("La raíz no puede ser un valor negativo")