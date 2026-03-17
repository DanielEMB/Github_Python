import random
import time
lista_palabrasecretafáciles = ["xaloc", "madrid",  "oceanía", "pedri", "saltar", "gato", "lápiz", "martes", "cinco", "papá"] 
lista_palabrasecretamedias = ["chocolate", "bisonte", "relatividad", "interstellar", "oceanía", "pokémon", "bisonte", "destrucción"] 
lista_palabrasecretadifíciles = ["desoxirribonucleico", "otorrinoralingólogo", "transanlántico", "permanganato", "mesopotamia", "arzobispado", "paracaidismo", "destrucción", "descomposición", "metanfetamina"]
lista_palabrasecretaextremas = ["anticonstitucionalmente", "esternocleidomastoideo", "hipopotomonstrosesquipedaliofobia", "pneumoultramicroscopicsilicovolcanoconiosis", "supercalifragilisticexpialioso", "parangaricutrimícuaro", "electroencefalografías", "paralelepípedoide", "microprocesador", "electrodoméstico"]
respuesta = "s"
numero = ""
partidas = 0
perdidas = 0
ganadas = 0
print("¡Bienvenido al juego del ahorcado!, introduce un número 1-4 para seleccionar tu dificultad.")
print("1. Fácil")
print("2. Media")
print("3. Difícil")
while numero != "1" and numero != "2" and numero != "3" and numero != "4":
    numero = input("Introduce un número del 1 al 4 para seleccionar tu dificultad: ")
    if numero == "1":
        lista_palabrasecreta = lista_palabrasecretafáciles
        print("Has seleccionado la dificultad fácil. ¡Que te diviertas!")
    elif numero == "2":
        lista_palabrasecreta = lista_palabrasecretamedias
        print("Has seleccionado la dificultad media, prepárate para un reto complicado")
    elif numero == "3":
        lista_palabrasecreta = lista_palabrasecretadifíciles
        print("Has seleccionado la dificultad difícil, buena suerte...")
    elif numero == "4":
        lista_palabrasecreta = lista_palabrasecretaextremas
        print("Has seleccionado la opción oculta, la dificultad extrema... ¿Listo para sufrir? ;)")
while respuesta == "S" or respuesta == "s":
    starttime = time.time()
    lista_partida = []
    lista_ahorcado = []
    lista_aciertos = []
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
                    lista_aciertos.append(letra)
                elif letra == "a" and palabra[i] == "á":
                    confirmador = 1
                    lista_partida[i] = "á"
                    lista_aciertos.append(letra)
                elif letra == "e" and palabra[i] == "é":
                    confirmador = 1
                    lista_partida[i] = "é"
                    lista_aciertos.append(letra)    
                elif letra == "i" and palabra[i] == "í":
                    confirmador = 1
                    print(confirmador)
                    lista_partida[i] = "í"
                    lista_aciertos.append(letra)
                elif letra == "o" and palabra[i] == "ó":
                    confirmador = 1
                    lista_partida[i] = "ó"
                    lista_aciertos.append(letra)
                elif letra == "u" and palabra[i] == "é":
                    confirmador = 1
                    lista_partida[i] = "ú"
                    lista_aciertos.append(letra)
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
    print("Has acertado", len(lista_aciertos), "letras")
    print("Has cometido", errores, "errores")
    end_time = time.time()
    duracion = end_time - starttime
    minutos = int(duracion // 60)
    segundos = int(duracion % 60)
    print("Tu partida ha durado", minutos, "minutos y", segundos, "segundos")
    partidas += 1
    confirmador == 0
    print(lista_partida)
    respuesta = input("¿Quieres jugar otra partida? s/n: ")
    lista_palabrasecreta.remove(palabra)
    palabrasecreta = ""
    while not palabrasecreta.islower() or palabrasecreta.isupper():
        palabrasecreta = input("Introduce una nueva palabra: ")
        palabrasecreta = palabrasecreta.lower()
        if palabrasecreta.isalpha() and palabrasecreta.islower():
            lista_palabrasecreta.append(palabrasecreta)
        else:
            print("¡Introduce una palabra válida!")           
