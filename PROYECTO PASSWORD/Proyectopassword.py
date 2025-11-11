# Mostrar las instrucciones de como ha de ser la contraseña
print("INSTRUCCIONES")
print("1.La longitud del password tiene que tener entre 6 i 8 carácteres")
print("2.Forzar los siguientes valores según la posición indicada")
print("     Posició 1 Un número major o igual a 1 i menor o igual que 5")
print("     Posició 2 Una letra minúscula")
print("     Posició 3 Una letra majúscula")
print("     Posició 4 Uno de los siguientes símbolos *, _, @")
print("     Posició 5 Una letra minúscula")
print("     Posició 6 Un número major o igual a 6 i menor o igual a 9")
print("     Posició 7 Uno de los siguientes símbolos &, /, #")
print("     Posició 8 Un número menos o igual a 5")
password = input("Introduce una palabra clave:")
passvalida = True
if len(password) >=6 and len(password) <=8:
    if password[0].isnumeric():
        passvalida = passvalida
        if int(password[0]) >=1 and int(password[0])<=5:
            #es necesario hacer esto, ya que si se da una condición no puedes poner otra condición
            #directamente sin que de error
            passvalida = passvalida
        else:
            print("Error en el carácter 1")
            passvalida = False
    else:
        print("Error en el carácter 1")
        passvalida = False
    if password[1].islower():
        passvalida = passvalida
    else:
        print("Error en el carácter 2")
        passvalida = False
    if password[2].isupper():
        passvalida = passvalida
    else:
        print("Error en el carácter 3")
        passvalida = False
    if password[3] in ["*", "_", "@"]:
        passvalida = passvalida
    else:
        print("Error en el carácter 4")
        passvalida = False
    if password[4].islower():
        passvalida = passvalida
    else:
        print("Error en el carácter 5")
        passvalida = False
    if password[5].isnumeric():
        passvalida = passvalida
        if  int(password[5]) >= 6 and int(password[5]) <= 9:
            passvalida = passvalida
            if len(password) == 6 and passvalida == True:
                # si todos los valores suman 6 carácteres y password es valida:
                print("el format del PASSWORD es CORRECTE")
        else:
            print("Error en el carácter 6")
            passvalida = False
    else:
        print("Error en el carácter 6")
        passvalida = False
    if len(password) >= 7:       
        if password[6] in ["&", "/", "#"]:
            passvalida = passvalida
            if len(password) == 7 and passvalida == True:
                # si todos los valores suman 7 carácteres y password es valida:
                print("el format del PASSWORD es CORRECTE")
        else:
            print("Error en el carácter 7")
            passvalida = False
    if len(password) == 8:
        if password[7].isnumeric():
            if int(password[7]) <= 5:
                if passvalida == True:
                    # si todos los valores suman 8 carácteres y password es valida:
                    print("el format del PASSWORD es CORRECTE")
            else:
                print("Error en el carácter 8")
        else:
            print("Error en el carácter 8")
            passvalida = False
else:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")