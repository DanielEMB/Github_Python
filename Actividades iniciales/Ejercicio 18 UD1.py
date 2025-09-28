#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.

menores = int(input("Introduce el número de menores de 18 años"))
mayores = int(input("Introduce el número de adultos"))

preciomenores = (12 * 0.5) * menores
preciomayores = (12 * 0.9) * mayores

print("El precio para los mayores de 18 es: ", preciomayores)
print("El precio para los menores de 18 es: ", preciomenores)