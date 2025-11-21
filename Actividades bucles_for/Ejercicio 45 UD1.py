#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:

palabra = input("Introduce una palabra")
vocales = ""
consonantes = ""

for i in range(0, len(palabra)):
    if palabra[i].isalpha():
        if palabra[i] in ["a", "e", "i", "o", "u"]:
            vocales = vocales + palabra[i]
        else:
            consonantes = consonantes + palabra[i]
print(f"Las vocales de la palabra {palabra} son: ", vocales)
print(f"Las consonantes de la palabra {palabra} son: ", consonantes)