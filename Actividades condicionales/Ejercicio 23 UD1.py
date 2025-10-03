#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

nota = float(input("Introduce la nota que has sacado"))

if nota <= 10 and nota >= 0:
    if nota >= 8.5:
        print("Has sacado un excelente, feñicidades!!!")
    elif nota >= 6.5: 
        print("Has sacado un notable!")
    else:
        print("Has suspendido.")
else:
    print("La nota que has introducido no está entre 0 y 10.")
