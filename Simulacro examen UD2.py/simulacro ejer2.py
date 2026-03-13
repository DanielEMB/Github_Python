contrasena = "abc123-Password1-1234-Admin2024-te@t"
lista = contrasena.split("-")

#control seguridad
for x in lista:
    numletras = 0
    numnumeros = 0
    numcaracteres = 0
    for j in x:
        if j.isnumeric():
            numnumeros+=1
        elif j.isalpha():
            numletras +=1
        else:
            numcaracteres +=1 #CARÁCTERES ESPECIALES
    # Tiene al menos x carácteres y contiene letras y números
    if numcaracteres == 0 and len(x)>= 8 and numletras>1 and numletras>1:
        print("la contraseña", x, "es segura")
    # Tiene menos de 8 carácteres. O solo contiene letras. O solo contiene números
    if numcaracteres == 0 and len(x)<8 and (numnumeros>=1 or numletras>=1):
        print("la contraseña", x, "es débil")
    # Tiene algún carácter especial
    if numcaracteres > 1:
        print("la contraseña", x, "es inválida")