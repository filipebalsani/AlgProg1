L = []
Ls = []
Lr = []

n = int(input("Quantos elementos tera a lista? "))

i=0

while i < n:
    x = int(input("add num to list: "))
    L.append(x)
    i+=1

i=0

while i < n:
    if len(Ls) == 0:
        y = L[0]
        Ls.append(y)
    else:
        j = 0
        igual = False
        while j < len(Ls):
            if L[i] == Ls[j]:
                igual = True
            j+=1
        if igual:
            z = L[i]
            Lr.append(z)
        else:
            z = L[i]
            Ls.append(z)
    i+=1

print(L)
print(Ls)
print(Lr)
