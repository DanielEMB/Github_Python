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
    for i in range(len(palabra)):
        if palabra[i] == letra:
            print("Letra encontrada:", letra, "en posición", i)
            lista_partida[i] = letra
    if not letra in palabra:
        lista_ahorcado.append(letra)
        print("Las letras incorrectas son:", lista_ahorcado)
    print(lista_partida)

