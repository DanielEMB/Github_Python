#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

nota = float(input("Introduce la nota que has sacado"))

if nota <= 10 and nota >= 0: 
    if nota >= 8.5:
         print("Has sacado un excelente, felicidades!!!")
    elif nota >= 6.5: 
        print("Has sacado un notable!")
    elif nota>= 5:
        print("Has sacado un satisfactorio")
    else:
        print("Has suspendido.")
else:
    print("La nota que has introducido no está entre 0 y 10.")