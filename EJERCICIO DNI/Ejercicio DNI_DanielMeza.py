# Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los
# siguientes puntos:
#  1.Controlar que el valor introducido tenga una longitud de 8 dígitos y sea numérico.
#  2.Visualizar el NIF completo, concatena la letra correspondiente separado con un guion: ej 11111111-R
#  3.Controlar aquellas situaciones en que el Resto obtenido de un DNI no aparece en la tabla, por tanto, es
#  incorrecto. Debe aparecer un mensaje de error.
#  4.Por cada cálculo que se realice, el programa debe ofrecer la opción de continuar o no, introduciendo
#  5.Las letras “s” o “n”. En caso de seleccionar “n” se visualiza MENÚ del apartado 7.

dni = input("Introduce solo los números de tu dni")
resto = 0
letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
if len(dni) == 8:
    resto = int(dni) % 23
    for i in range(len(letras)):
        if letras[i] == letras[resto]:
            dni +=  "-" + letras[i]
print(dni)
