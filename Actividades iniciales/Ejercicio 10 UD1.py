#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

var1 = float(input("Introduce un valor"))
var2 = float(input("Introduce otro valor"))

cociente = var1/var2
resto = var1 % var2
if resto == 0:
    dividendo = "par"
else:   
    dividendo = "impar"
print("El cociente es:", cociente)
print("El resto es:", resto)
print("El dividendo es", dividendo) 