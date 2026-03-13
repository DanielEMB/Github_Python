import random

lista_palabrasecreta = ["xaloc", "sacapuntas", "chocolate", "bisonte", "relatividad", "desoxirribonucleico", "pokémon", "interstellar", "oceanía", "pedri"]
respuesta = "s"
partidas = 0
perdidas = 0
ganadas = 0
while respuesta == "S" or respuesta == "s":
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
    while lista_partida != lista_palabra and errores != 8:
        lista_palabra = list(palabra)
        letra = input("Introduce una letra: ")
        if len(letra) != 1 and letra.isalpha():
            print("Introduce solo una letra!")
        elif letra in lista_partida and confirmador == 0 and len(letra) == 1:
            print("Ya has introducido esta letra antes")
        else:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    print("Letra encontrada:", letra, "en posición", i)
                    lista_partida[i] = letra
                elif letra == "a" and palabra[i] == "á":
                    confirmador == 1
                    lista_partida[i] = "á"
                elif letra == "e" and palabra[i] == "é":
                    confirmador == 1
                    lista_partida[i] = "é"
                elif letra == "i" and palabra[i] == "í":
                    confirmador == 1
                    print(confirmador)
                    lista_partida[i] = "í"
                elif letra == "o" and palabra[i] == "ó":
                    confirmador == 1
                    lista_partida[i] = "ó"
                elif letra == "u" and palabra[i] == "é":
                    confirmador == 1
                    lista_partida[i] = "ú"
            print(lista_partida)
        if not letra in palabra and confirmador == 0 and len(letra) == 1: # INTRODUCIDO PALABRA INCORRECTA
            print("Has introducido una letra incorrecta!")
            if not letra in lista_errores:  #LETRAS AHORCADO CUANDO INTRODUCES VALOR INCORRECTO
                errores+=1
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
        perdidas += 1
    else:
        print("¡Enhorabuena! Has ganado.")
        ganadas += 1
    partidas += 1
    confirmador == 0
    print(lista_partida)
    #RECUERDA SUBIR EJERCICIOS JUTGE EN EL REPOSITORIO
    respuesta = input("¿Quieres jugar otra partida? s/n: ")
    print(respuesta)