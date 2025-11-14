# 46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
# palabra Abrigo utilizando únicamente una instrucción.

palabra = input("Introduce una palabra")
vocales = ""
consonantes = ""
palabra = palabra.lower()
for i in range(0, len(palabra)):
    if palabra[i].isalpha():
        if palabra[i] in ["a", "e", "i", "o", "u"]:
            vocales = vocales + palabra[i]
        else:
            consonantes = consonantes + palabra[i]
print(f"Las vocales de la palabra {palabra} son: ", vocales)
print(f"Las consonantes de la palabra {palabra} son: ", consonantes)