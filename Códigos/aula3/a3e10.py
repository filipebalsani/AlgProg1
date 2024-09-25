n = float(input("Numero N: "))
i = 2
#numerador = 1*x
#divisor = x*2 - 1
s = 0

print("S = 1 ", end='')
while i <= n:
    num = (i)
    div = i*2 - 1
    print(f"+ {num}/{div} ",end='')
    s = float(s + num / div)
    i = i + 1

print(f"\nSoma = {s+1}")
