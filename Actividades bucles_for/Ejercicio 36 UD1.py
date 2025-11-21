# 36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

n = int(input("Introduce los números naturales que quieres que se sumen"))
sumatotal = 0
for i in range(0, n):
    sumatotal = sumatotal + (n - i)
print("La suma de los números es: ", sumatotal)