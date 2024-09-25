L=[]
Lq=[]
n = int(input("Quantos elementos tera a lista? "))

i=0
while i < n:
    x = int(input("add num to list: "))
    L.append(x)
    i+=1

i=0
while i < n:
    y = L[i]**2
    Lq.append(y)
    i+=1

print(L)
print(Lq)
