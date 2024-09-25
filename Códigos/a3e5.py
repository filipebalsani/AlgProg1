n = int(input("numero maior que 1: "))
x = n
c = 0
while x > 0:
    if n%x == 0:
        c = c + 1
    x = x - 1

if c == 2:
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")

