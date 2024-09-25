L = []
La = []
n = int(input("Quantos elementos tera a lista (valores positivos apenas)? "))


i=0
while i < n:
    x = int(input("add num to list: "))
    L.append(x)
    i+=1

i=0
while i < n:
    
    y = L[i]

    if y % 2 == 0: # par
        La.append(1)
    else: # ímpar
        La.append(-1)
    i+=1

print(L)
print(La)
