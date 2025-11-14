# 43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
# por pantalla cada letra

palabra = input("Introduce una palabra")

for i in range (0, len(palabra)):
    print(f"En la posición {i} está la letra: ", palabra[i])
    #NOTAS: len(palabra) se refiere a la longitud de la palabra, para que el buclse se repita ese numero de veces
    # f"en la posición{i}, lo hacemos para que cada posicion salga, y después junto a la letra de la posición
    # de "i" en la palabra.