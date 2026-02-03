# Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los
# siguientes puntos:
#  1.Controlar que el valor introducido tenga una longitud de 8 dígitos y sea numérico.
#  2.Visualizar el NIF completo, concatena la letra correspondiente separado con un guion: ej 11111111-R
#  3.Controlar aquellas situaciones en que el Resto obtenido de un DNI no aparece en la tabla, por tanto, es
#  incorrecto. Debe aparecer un mensaje de error.
#  4.Por cada cálculo que se realice, el programa debe ofrecer la opción de continuar o no, introduciendo
#  5.Las letras “s” o “n”. En caso de seleccionar “n” se visualiza MENÚ del apartado 7.

resto = 0
letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
lista_dni = []
respuesta = "s"

dni_correctos = []
dni_incorrectos = []
erroreslongitud = 0
erroresnumerico = 0
errorestotal = 0
num_dnicorrectos = []
while respuesta == "s":
    dni = input("Introduce solo los números de tu dni")
    if len(dni) != 8:
        print("El DNI no cumple la longitud de 8 dígitos.")
        lista_dni.append(0)
        dni_incorrectos.append(dni)
        erroreslongitud += 1
        errorestotal += 1
    if dni.isnumeric():
        if len(dni) == 8:
            resto = int(dni) % 23
            for i in range(len(letras)):
                if letras[i] == letras[resto]:
                    dni +=  "-" + letras[i]
            lista_dni.append(3)
            dni_correctos.append(dni)
            print("¡DNI correcto!")
    else:
        lista_dni.append(1)
        dni_incorrectos.append(dni)
        print("El dni introducido tiene que ser numérico.")
        erroresnumerico += 1
        errorestotal += 1
    respuesta = input("¿Quieres introducir otro DNI? s/n: ")
dni_correctos.sort()
dni_incorrectos.sort()
# imprimir dni correctos, incorrectos, num de errores total, num total de dni correctos, % de DNI correctos,
# incorrectos, errores de longitud, errores de número, no existentes.
print("RESULTADOS. Escoge una opción."), print("1. listar DNI correcto ordenado de menor a mayor")
print("2. Listar DNI incorrecto ordenado de menor a mayor"), print("3. Número total de errores producidos")
print("4. Número total de DNI correctos"), print("5. Porcentajes intentos con error y sin error"),
print("6. Salir s/n")
opción = int(input("Escoje una opción para mostrarse en la salida 1-7"))
if opción == 1:
    print("Los DNI correctos de menor a mayor son:", dni_correctos)
if opción == 2:
    print("Los DNI incorrectos de menor a mayor son:", dni_incorrectos)
if opción == 3:
    print(f"Has tenido {errorestotal} errores")
if opción == 4:
    aciertos = len(dni_correctos)
if opción == 5:
    aciertos = len(dni_correctos)
    errores = len(dni_incorrectos)
    intentos = errores + aciertos
    correctos = aciertos/ intentos * 100
    incorrectos = errores / intentos * 100
    print("El porcentaje de DNI correctos es: ", correctos)
    print("El porcentaje de incorrectos es: ", incorrectos)
