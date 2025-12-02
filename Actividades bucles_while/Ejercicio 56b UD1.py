# 56b. Haz alguna o todas las mejoras en el programa anterior que a continuación se 
#indican:
#- Cuando se pregunta “si desea realizar otro pedido”, el encargado puede introducir s ó n en 
#mayúscula o minúscula.
#- Si el encargado introduce otro valor distinto a S o N, el programa debe repetir la pregunta e 
#informar de que ha introducido un valor equivocado.
#- El lugar de almacenar los precios en variables, utiliza una biblioteca (busca información) 
#e investiga como moverte por los índices.
#- Un pedido puede estar formado por 3, 2 o 1 componentes. Ej. Un usuario puede pedir únicamente
#una bebida.

print("MENÚ"), print("1. Bocadillo de calamares- 9 €"), print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €"), print("ACOMPAÑAMIENTO"), print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €"), print("3. Patatas rústicas - 2 €"), print("BEBIDAS")
print("1. Coca cola - 2 €"), print("2. Acuarius - 1.5 €" ), print("3. Agua - 1 €")

pedidos = 0
totalapagar = 0
respuesta = "s"
while respuesta == "s":
    bebida = int(input("Introduce tu bebida"))
    #GESTIÓN BOCATAS
    bocadillo_ = input("¿Quieres bocadillo? s/n: ")
    if bocadillo_ == "s" or "S": 
        bocadillo = int(input("Introduce tu bocadillo"))
        if bocadillo == 1:
            totalapagar += 9
        elif bocadillo == 2:
            totalapagar += 4.5
        elif bocadillo == 3:
            totalapagar += 2.5
    #GESTIÓN ACOMPAÑAMIENTO
    acompañamiento_ = input("Quieres acompañamiento? s/n:" ) 
    if acompañamiento_ == "s" or "S":
        acompañamiento = int(input("Introduce tu acompañamiento"))
        if acompañamiento == 1:
            totalapagar += 1.5
        elif acompañamiento == 2:
            totalapagar += 1.75
        elif acompañamiento == 3:
            totalapagar += 2
    #GESTIÓN BEBIDAS
    bebida_ = input("Quieres bebida? s/n: ")
    if bebida_ == "s" or "S":
        if bebida == 1:
            totalapagar += 2
        elif bebida ==2:
            totalapagar += 1.5
        elif bebida ==3:
            totalapagar += 1
    respuesta = input("Quieres gestionar otro pedido? s/n: ")
    while not respuesta == "s" or "S" or "n" or "N": # Condición 2, para repetir la pregunta.
        respuesta = input("Quieres gestionar otro pedido? s/n: ")
    respuesta = respuesta.lower() # Condición uno, para que siempre se convierta minúscula.
totalconIVA = round(totalapagar * 1.1, 2)
print("Total a pagar: ", totalapagar)
print("Total con IVA: ", totalconIVA)
if totalapagar >= 20 and totalapagar <= 30:
    totalcondescuento = totalconIVA * 0.95
    print("Total con descuento del 5%: ", totalcondescuento)
if totalapagar > 30:
    totalcondescuento = totalconIVA * 0.85
    print("Total con descuento del 15%: ", totalcondescuento)