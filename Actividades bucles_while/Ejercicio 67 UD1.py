# 67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes 
# consideraciones:
# Debe tener una longitud entre 6 y 8 caracteres.
# Debe contener como mínimo:
# 2 números mayores o iguales que 1 y menor o igual que 5
# 2 letras minúsculas
# 1 letra mayúscula
# 2 símbolos (*, _, @, &,/,#)
# 1 número mayor o igual que 6 y menor o igual que 5
print("Introduce una contraseña que cumpla las siguientes condiciones:"), print(" - Longitud entre 6 y 8 caracteres"),
print(" - Al menos 2 números entre 1 y 5"), print(" - Al menos 2 letras minúsculas"), print(" - Al menos 1 letra mayúscula"),
print(" - Al menos 2 símbolos (*, _, @, &,/,#)"), print(" - Al menos 1 número entre 6 y 9-")
password = input("Introduce una contraseña: ")
longitud = len(password)
passcorrecta = True
#VARIABLES CONTADORAS
contador_numeros_entre1y5 = 0
contador_minusculas = 0
contador_mayusculas = 0
contador_simbolos = 0
contador_numeros_entre6y9 = 0
#CONDICIÓN 1
if 6 <= longitud <= 8:
    #CONDICIÓN 2
    contador_numeros_entre1y5 = 0
    for i in range(longitud):
        if password[i] in "12345":
            contador_numeros_entre1y5 += 1
    if contador_numeros_entre1y5 >= 2:
        #CONDICIÓN 3   
        for i in range(longitud):
            if password[i] in "abcdefghijklmnñopqrstuvwxyz":
                contador_minusculas += 1
        if contador_minusculas >= 2:
            #CONDICIÓN 4
            for i in range(longitud):
                if password[i] in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
                    contador_mayusculas += 1
            if contador_mayusculas >= 1:
                #CONDICIÓN 5
                for i in range(longitud):
                    if password[i] in "*_@&/#":
                        contador_simbolos += 1
                if contador_simbolos >= 2:
                    #CONDICIÓN 6
                    for i in range(longitud):
                        if password[i] in "6789":
                            contador_numeros_entre6y9 += 1
                    if contador_numeros_entre6y9 >= 1:
                        passcorrecta = True
                    else:
                        passcorrecta = False
                else:
                    passcorrecta = False
            else:
                passcorrecta = False
        else:
            passcorrecta = False
    else:
        passcorrecta = False
else:
    passcorrecta = False
if passcorrecta == True:
    print("Contraseña válida")
else:
 print("Contraseña inválida")