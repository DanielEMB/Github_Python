import math
letra = input("que deseas Matúscula(M)o minúscula(m)? ")
radio = int(input("Introduce el radio: "))
altura = int(input("Introduce altura: "))

fórmula = round (((math.pi * radio**2)*altura), 3)
if letra not in ("Mm"):
    print("error")
elif letra == "M":
    print("EL VOLUMEN ES:", fórmula)
else:
    print("el volumen es:", fórmula)