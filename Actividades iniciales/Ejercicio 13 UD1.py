#13. Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.

lado = float(input("Inroduce el lado del cubo"))
área = lado*lado * 6
volumen = lado** 3

print("El área es:", área)
print("El volumen es:", volumen)