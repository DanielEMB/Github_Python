#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años

frase = "No hay mal que dure cien años"
fraselower = frase.lower()
vocales = "aeiou" 
for vocal in vocales:
    print(f"el número de {vocal}'s es:{fraselower.count(vocal)}")