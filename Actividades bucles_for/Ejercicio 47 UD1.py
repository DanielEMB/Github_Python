# 47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
# mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
# la secuencia en descenso. Respeta el formato de salida

intervalo1 = int(input("Introduce el primer intérvalo"))
intervalo2 = int(input("Introduce el segundo intérvalo"))

numeros = ""
if intervalo1 < intervalo2:
    for i in range(intervalo1, intervalo2 + 1):
        numeros = numeros + str(i) + "-" 
elif intervalo1 > intervalo2:
    for i in range(intervalo2, intervalo1, -1):
        numeros = numeros+ str(i) + "-" 
else:
    print(intervalo1)
print(numeros)