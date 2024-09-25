L=[]
L1=[]
L2=[]

n = int(input("Quantos elementos tera a lista? "))
print("LISTA 1:")
i = 0
while i<n:
    x = int(input("add num to list 1: "))
    L1.append(x)
    i+=1

print("LISTA 2:")
i = 0
while i<n:
    x = int(input("add num to list 2: "))
    L2.append(x)
    i+=1


i = 0
while i<n:
    x = L1[i]+L2[i]
    L.append(x)
    i+=1

print(L1)
print(L2)
print(L)
