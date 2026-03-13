import math
x = float(input())
suelo = math.floor(x)
techo = math.ceil(x)
if x >= 0: #SI ES NEGATIVO
    redondeo = math.floor(x + 0.5)
else:
    redondeo = math.ceil(x - 0.5)

print(suelo, techo, redondeo)