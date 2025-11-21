# 54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
# de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
# preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
# operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
# mensaje del acumulado es singular o plural.. . Con While
sumatotal = 0
repeticiones = 0
while sumatotal< 50:
    numero1 = int(input("Introduce el 1er número: "))
    numero2 = int(input("Introduce el 2ndo número: "))
    suma = numero1 + numero2
    print("El resultado de la suma es: ", suma)
    sumatotal += suma
    repeticiones += 1
    if repeticiones == 1:
        print(f"El total acumulado es: {sumatotal} y llevas {repeticiones} operación realizada.")
    else:
        print(f"El total acumulado es: {sumatotal} y llevas {repeticiones} operaciones realizadas.")

print("Fin del programa")
