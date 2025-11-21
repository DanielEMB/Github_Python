# 56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
# compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
# dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
# visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
# realización de un pedido, si quiere gestionar otro. 

print("MENÚ"), print("1. Bocadillo de calamares- 9 €"), print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €"), print("ACOMPAÑAMIENTO"), print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €"), print("3. Patatas rústicas - 2 €"), print("BEBIDAS")
print("1. Coca cola - 2 €"), print("2. Acuarius - 1.5 €" ), print("3. Agua - 1 €")

pedidos = 0
bocadillo = int(input("Introduce tu bocadillo"))
acompañamiento = int(input("Introduce tu acompañamiento"))
bebidas = int(input("Introduce tu bebida"))