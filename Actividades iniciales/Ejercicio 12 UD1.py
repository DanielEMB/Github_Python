#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

print("Me vas a inroducir los datos necesarios para que te calcule el área y perímetro de un trapecio isósceles")
lado = float(input("Introduce el lado"))
basemenor = float(input("Introduce la base menor"))
basemayor = float(input("Introcude la base mayor"))
altura = float(input("Introuduce la altura"))

perímetro = lado*2 + basemenor + basemayor
área = (basemayor + basemenor) / 2 * altura
print("El perímetro es:", perímetro)
print("El área es:", área)