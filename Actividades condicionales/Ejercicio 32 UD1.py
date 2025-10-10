#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas

frase = ("A quién madruga Dios ayuda")
palabra = input("Introduce la palabra que quieres comprobar")
fraselower = frase.lower()
palabra = palabra.lower()
index = fraselower.find(palabra)
if not index == -1:
    print(f"La palabra está en la frase y en el index {index}")
else:
    print("La palabra no está en la frase")