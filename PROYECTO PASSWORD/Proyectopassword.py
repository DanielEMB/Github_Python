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

if len(password) >=6 and len(password) <=8:
    if password[0] >= 1:
        if password[1].islower:
            if password[2].isupper:
            
            else:
            print("Error en el caràcter 3")
        else:
            print("Error en el caràcter 2")
    else:
        print("Error en el caràcter 1")
else:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits”")