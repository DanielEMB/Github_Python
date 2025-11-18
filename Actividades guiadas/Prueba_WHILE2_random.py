import random

num_secreto = random.randint(1,20)
print(num_secreto)

numero= int(input("Introduce un número del 1 al 20:"))

while num_secreto!=numero:
    # num_secreto = random.randint(1,20)
    if (numero>0 and numero<=20):
        print(f"has introducido el numero {numero}, pero no has acertado")
    else:
        print("El número introducido está fuera del rango")
    numero = int(input("vuelve a introducir un valor"))

print("Has acertadoo!!")
