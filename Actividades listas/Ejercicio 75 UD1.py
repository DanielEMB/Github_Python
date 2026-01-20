# 75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
# pantalla los siguientes resultados:
# a. Cantidad total de valores, b. Cantidad de números, c. Cantidad de letras d. Cantidad de mayúsculas
# e. Suma de los valores numéricos
lista1 = ["a","b","D","x","r","X","3","h","w","2","i"]
valores = 0
numeros = 0
letras = 0
mayus = 0
sumatotal = 0

for i in lista1:
    valores += 1
    if i.isnumeric():
        numeros += 1
        sumatotal += int(i)
    elif i.isalpha():
        letras += 1
        if i.isupper():
            mayus +=1
print("Número de valores: ", valores)
print("Cantidad de números: ", numeros)
print("Cantidad de letras: ", letras)
print("Cantidad de mayúsculas: " , mayus)
print("Suma total de números: ", sumatotal)
