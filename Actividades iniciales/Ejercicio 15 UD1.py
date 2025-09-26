#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio = float(input("Introduce el radio del cilindro"))
altura = float(input("Introduce la altura"))

área = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * (radio**2) * altura

print("El área es:", round(área, 2))
print("El volumen es:", round(volumen, 2))