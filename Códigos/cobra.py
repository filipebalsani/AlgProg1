c = int(input("numero de 4 digitos: "))
print(c)
x = c
i = 1
f = 0
exp = 3
while x > 10:
    if x - i*10**exp < 10**exp:
        x = x - i*10**exp
        exp = exp - 1
        i = 1
        if f == 0:
            c = c - x
            f = f + 1
        print(x)
    i = i + 1
if x == c/1000:
    print("F")
else:
    print("V")
