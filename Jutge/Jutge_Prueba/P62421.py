lista = []
palabras = input()
lista = palabras.split(" ")
lista.reverse()
reversa = ""
for i in range(0, 3):
    reversa += lista[i] + " "
print(reversa[:-1])