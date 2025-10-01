#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división).

import math
valor = float(input("Introduce un número para calcular su raíz cuadrada"))
raízcuadrada = math.sqrt(valor)
división = raízcuadrada // 2
print("La raíz cuadrada es:", raízcuadrada)
print("La división de la raíz cuadrada entre 2 es:", división)