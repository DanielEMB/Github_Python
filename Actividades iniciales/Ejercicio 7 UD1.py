#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

var1 = int(input("Introduce un número"))
var2 = int(input("Introduce el otro número"))

suma = var1 + var2
resta = var1 - var2
multiplicación = var1 * var2
división = var1/var2
exponente = var1 ** var2
módulo = var1 % var2
división_entera = var1 // var2

print("La suma entre operador1 y operador 2 es ", suma)
print("La resta entre operador1 y operador 2 es ", resta)
print("La multiplicación entre operador1 y operador 2 es ", multiplicación)
print("La división entre operador1 y operador 2 es ", round(división, 2))
print("El exponente entre operador1 y operador 2 es ", exponente)
print("La módulo entre operador1 y operador 2 es ", módulo)
print("La división entera emtre entre operador1 y operador 2 es ", división_entera)