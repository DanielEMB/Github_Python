#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual,
#  menor o mayor de 11 caracteres. Utiliza elif

frase = input("Introduce una frase")
longitudfrase = len(frase)

if longitudfrase > 11:
    print("La longitud de la frase es mayor que 11 carácteres")
elif longitudfrase < 11:
    print("La longitud de la frase es mayor que 11 carácteres")
else:
    print("La longitud de la frase es de 11 carácteres")