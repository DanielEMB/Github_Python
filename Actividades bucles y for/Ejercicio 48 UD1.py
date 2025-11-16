# 48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de
# esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
# tenga x oportunidades para ver si letra introducida está en esa palabra.

palabrasecreta = input("Introduce tu palabra secreta")
longitud = len(palabrasecreta)
oportunidades = longitud
# facil, un bucle que tenga de numero de veces de repetir la longitud de la palabrasecreta
# si la letra esta en la palabra, decimos que existe, si no, decimos que no existe
for i in range(0, oportunidades):
    letra = input("Introduce una letra: ")
    if letra in palabrasecreta:
        print("La letra", letra, "existe")
    else:
        print("La letra", letra, "no existe.")