temperatura = int(input())
if temperatura > 30:
    print("it's hot")
    if temperatura >=100:
        print("water would boil")
if temperatura <= 30 and temperatura >= 10:
    print("it's ok")
if temperatura < 10:
    print("it's cold")
    if temperatura <= 0:
        print("water would freeze")