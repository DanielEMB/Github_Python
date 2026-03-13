letra = input()
mayus = ""
vocal = ""
if letra.islower():
    mayus = "lowercase"
elif letra.isupper():
    mayus = "uppercase"
if letra in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    vocal = "vowel"
else:
    vocal = "consonant"
print(mayus)
print(vocal)