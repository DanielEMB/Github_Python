letra = input()
if letra.islower():
    letra = letra.upper()
elif letra.isupper():
    letra = letra.lower()
print(letra)