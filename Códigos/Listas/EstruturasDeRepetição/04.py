import random

n = random.randint(1,100)
g = 0
c = 1

while g != n:
    g = int(input("Adivinhe o numero entre 1 e 100: "))
    if g == n:
        print(f"Número correto! Tentativas: {c}")
    elif g > n:
        print("Número incorreto, tente um valor menor")
        c = c + 1
    else:
        print("Número incorreto, tente um valor maior")
        c = c + 1



