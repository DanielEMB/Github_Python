#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
radio = float(input("Introduce el radio del círculo"))
perímetro = 2* radio * math.pi
área = math.pi * radio**2

print("El perímetro es:", round(perímetro, 1))
print("El área es:", round(área, 1))