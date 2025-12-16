#MODIFICACIONES PENDIENTES para PASSWORD 2:
print("INSTRUCCIONES")
print("1. Como mínimo 3 números(distinguiendo rangos), 3 letras y 2 símbolos.")
print("2. Mínimo 1 mayúscula y 2 minúsculas."), print("3. Mínimo un numero entre 6 y 9 y dos del 1 al 5.")
print("4. Bucle que recorra el password y realice las comprobaciones y los contajes necesarios.")
print("5. Introducir 3 password en total, salida que aparezca el núm de contraseñas correctas e incorrectas.")
print("6. Testeo de 10 pruebas que permita la evaluación del código.")
# Tienes la libertad de hacer las modificaciones que quieras, siempre que las indiques claramente.
# Entrega límite para Viernes 20.

# CONTADORES
contador = 0
contraseñas = ""

while contador < 3:
    # VARIABLES DE CONDICIONES
    numeros = 0 # uno del 6-9, dos 1-5
    numerosA = 0
    numerosB = 0
    mayus = 0 # 1 mínimo
    minus = 0 # 2 mínimo
    simbolos = 0
    letras = 0    

    password = input("Introduce tu password: ")
    correcta = True
    contador +=1
    for i in range(len(password)):
        if password[i].isnumeric():
            numeros += 1
            if int(password[i]) >= 6: # DETECTAR Q SOLO SEA 1
                numerosA += 1
            elif int(password[i]) <= 5: # DETECRAR Q SOLO SEAN 2
                numerosB += 1
        elif password[i].isalpha():
            letras += 1
            if password[i].isupper():
                mayus += 1
            elif password[i].islower():
                minus += 1
        else:
            simbolos += 1      
    if numeros<3:
        correcta = False
    if letras<3:
        correcta = False
    if minus<2:
        correcta = False
    if mayus<1:
        correcta = False
    if simbolos<2:
        correcta = False
    if numerosA<1:
        correcta = False
    if numerosB<2:
        correcta = False
    if correcta == True:
        contraseñas += (f"Contraseña {contador} correcta, ")
    else:
        contraseñas += (f"Contraseña {contador} incorrecta, ")
print(contraseñas[:-2] + ".")
#ERROR CON ESTA CONTRASEÑA: Ddd239#@