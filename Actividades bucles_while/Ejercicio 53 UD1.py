# 53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
# sumas y el número de repeticiones. Con While.
repetir = ""
sumatotal = 0
repeticionestotal = 0
while repetir == "s" or repetir == "":
    numero1 = int(input("Introduce el 1er número: "))
    numero2 = int(input("Introduce el 2ndo número: "))
    suma = numero1 + numero2
    print("El resultado de la suma es: ", suma)
    repetir = input("deseas repetir la operación? s/n: ")
    sumatotal += suma
    repeticionestotal += 1
print("Resumen:")
print(f"La suma total es: {sumatotal} y el número de repeticiones es: {repeticionestotal}")
