x = int(input("numero maior ou igual a 0: "))

n = int(x)
while n > 0:
    d = 2
    while d >= 2:
        if n%d == 0:
            print(f"{n} / {d} = {int(n/d)}")
            n = int(n/d)
            d = 1
        else:
            d = d + 1
        if n == 1 :
            n = 0

            
