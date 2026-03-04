import random

lista_palabrasecreta = ["xaloc", "sacapuntas", "chocolate", "bisonte", "relatividad", "desoxirribonucleico", "pokémon", "interstellar", "oceanía", "pedri"]
lista_partida = []
lista_ahorcado = []

lista_errores = []
errores = 0
lista_palabra = []
palabra = random.choice(lista_palabrasecreta)
for i in range(len(palabra)):
    lista_partida += "_"
print(lista_partida)
confirmador = 0
while lista_partida != lista_palabra:
    lista_palabra = list(palabra)
    letra = input("Introduce una letra: ")
    if letra in lista_partida and confirmador == 0 and len(letra) == 1:
        print("Ya has introducido esta letra antes")
    else:
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
    if not letra in palabra and confirmador == 0: # INTRODUCIDO PALABRA INCORRECTA
        print("Has introducido una letra incorrecta!")
        errores+=1
        if not letra in lista_errores:  #LETRAS AHORCADO CUANDO INTRODUCES VALOR INCORRECTO
            lista_errores.append(letra)
            if errores == 1:
                lista_ahorcado.append("A")
            if errores == 2:
                lista_ahorcado.append("H")
            if errores == 3:
                lista_ahorcado.append("O")
            if errores == 4:
                lista_ahorcado.append("R")
            if errores == 5:
                lista_ahorcado.append("C")
            if errores == 6:
                lista_ahorcado.append("A")
            if errores == 7:
                lista_ahorcado.append("D")
            if errores == 8:
                lista_ahorcado.append("O")
            print(lista_ahorcado)
        else:
            print("Ya has introducido esta letra antes")
        print("Las letras incorrectas son:", lista_errores)
        if errores == 8:
            print("...")
            print("FIN DE LA PARTIDA. HAS PERDIDO :(")
            break
    confirmador == 0
    print(lista_partida)
    #RECUERDA SUBIR EJERCICIOS JUTGE EN EL REPOSITORIO