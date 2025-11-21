# 55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
# haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
# cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While.
sumatotal = 0
repeticiones = 0
while sumatotal < 50 or suma%2 == 0:
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

