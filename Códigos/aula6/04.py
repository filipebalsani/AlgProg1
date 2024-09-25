def Numero(n):
    if n > 0:
        return 1
    else:
        if n == 0:
            return 0
        else:
            return -1

num = int(input("Numero: "))

r = Numero(num)

print(r)
