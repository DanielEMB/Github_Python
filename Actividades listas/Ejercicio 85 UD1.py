# 85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres
# asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el
# programa debe mostrar la media y mediana los todos los alumnos introducidos
catalan = []
ingles = []
castellano = []
masalumnos = "s"
cantidadalumnos = 0
while masalumnos == "s":
        estudiante = input("Introduce estudiante: ")
        i = 0
        nota_catalan = float(input(f"Introduce la nota de catalán del alumno {i+1}: "))
        nota_ingles = float(input(f"Introduce la nota de inglés del alumno {i+1}: "))
        nota_castellano = float(input(f"Introduce la nota de castellano del alumno {i+1}: "))
        catalan.append(nota_catalan)
        ingles.append(nota_ingles)
        castellano.append(nota_castellano)
        i+=1 
        masalumnos = input("¿Quieres introducir las notas de otro alumno? s/n: ")
        cantidadalumnos += 1
        media_catalan = sum(catalan) / cantidadalumnos
        media_ingles = sum(ingles) / cantidadalumnos
        media_castellano = sum(castellano) / cantidadalumnos
# FALTAN LAS MEDIANAS


