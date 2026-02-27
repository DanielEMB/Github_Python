import random

lista_palabrasecreta = ["xaloc", "sacapuntas", "chocolate", "bisonte", "relatividad", "desoxirribonucleico", "pokémon", "interstellar", "oceanía", "pedri"]
lista_partida = []
lista_ahorcado = []

palabra = random.choice(lista_palabrasecreta)
for i in range(len(palabra)):
    lista_partida += "_"
print(lista_partida)
confirmador = 0
while lista_partida != palabra:
    letra = input("Introduce una letra")
    for i in range(len(palabra)):
        if palabra[i] == letra:
            print("Letra encontrada:", letra, "en posición", i)
            lista_partida[i] = letra
        elif letra == "a":
            confirmador == 1
            if "á" in letra:
                lista_partida[i] = "á"
        elif letra == "e":
            confirmador == 1
            if "é" in letra:
                lista_partida[i] = "é"
        elif letra == "i":
            confirmador == 1
            if "í" in letra:
                lista_partida[i] = "í"
        elif letra == "o":
            confirmador == 1
            if "ó" in letra:
                lista_partida[i] = "ó"
        elif letra == "u":
            confirmador == 1
            if "ú" in letra:
                lista_partida[i] = "ú"
    if not letra in palabra and confirmador == 0:
        lista_ahorcado.append(letra)
        print("Las letras incorrectas son:", lista_ahorcado)
    confirmador == 0
    print(lista_partida)

