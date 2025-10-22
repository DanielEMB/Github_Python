#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

frase = ("A quién madruga Dios ayuda")
palabra = input("Introduce la palabra que quieres comprobar")
index = frase.find(palabra)
if not index == -1:
    print(f"La palabra está en la frase y en el index {index}")
else:
    print("La palabra no está en la frase")