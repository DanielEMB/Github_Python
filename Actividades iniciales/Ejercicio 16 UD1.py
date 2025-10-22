#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).

import math
var1 = float(input("Introduce un número para calcular la raíz cuadrada"))
raiz = math.sqrt(var1)
resultado = raiz / 2 
print("El resultado de la raíz es:", raiz)
print("El resultado de la división es:", round(resultado, 1))