# 44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
# de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ",".
numeros = "" #queremos que la variable sea tipo string, para que le vayamos sumando 3 y se vayan juntando como texto
for i in range(0, 100, 3):
    numeros = numeros + str(i) + "," 
print(numeros)