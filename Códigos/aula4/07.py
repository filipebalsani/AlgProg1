L = []
Li = []
n = int(input("Quantos elementos tera a lista? "))


i=0
while i < n:
    x = int(input("add num to list: "))
    L.append(x)
    i+=1

i = len(L)
while i > 0:
    i-=1
    y = L[i]
    Li.append(y)

print(L)
print(Li)
    
