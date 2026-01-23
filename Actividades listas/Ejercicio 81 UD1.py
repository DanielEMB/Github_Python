# 81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la 
# lista al azar.
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
import random
numrandom = random.randint(0, 7)
print(lista[numrandom])