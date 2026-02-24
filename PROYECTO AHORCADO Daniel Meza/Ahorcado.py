import random

lista_palabrasecreta = ["xaloc", "sacapuntas", "chocolate", "bisonte", "relatividad", "desoxirribonucleico", "pokémon", "interstellar", "oceanía", "pedri"]
lista_partida = []
lista_ahorcado = []

palabra = random.choice(lista_palabrasecreta)
for i in range(len(palabra)):
    lista_partida += "_"
print(lista_partida)

while lista_partida != palabra:
    letra = input("Introduce una letra")
    if letra in palabra:
        for i in palabra:
            if letra == i:
                posicion = palabra.index(i)
                print(posicion)