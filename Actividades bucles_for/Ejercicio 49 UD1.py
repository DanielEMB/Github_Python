# 49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te
# indique en qué posición de la palabra se encuentra la letra.

palabrasecreta = input("Introduce tu palabra secreta")
longitud = len(palabrasecreta)
oportunidades = longitud
# facil, un bucle que tenga de numero de veces de repetir la longitud de la palabrasecreta
# si la letra esta en la palabra, decimos que existe, si no, decimos que no existe
for i in range(0, oportunidades):
    letra = input("Introduce una letra: ")
    if letra in palabrasecreta:
        print("La letra", letra, "existe")
        print("La letra está en la posición/es:")

        # Recorremos la palabra 1 a 1 para buscar la letra o las letras
        posicion = 1  # Para contar desde el carácter 1.
        for caracter in palabrasecreta:
            if caracter == letra:
                print(posicion)
            posicion = posicion + 1
    else:
        print("La letra", letra, "no existe.")
