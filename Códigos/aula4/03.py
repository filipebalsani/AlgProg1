L=[]

stop = True

while stop:
    numero = int(input("add num to list (-1 to stop): "))
    if numero == -1:
        stop = False
    else:
        L.append(numero)
i=0
soma=0
multi=1

while i<len(L):
    if L[i] % 2 == 0:
       soma+=L[i]
       i+=1
    else:
        multi*=L[i]
        i+=1

print(L)
print(f"Soma dos pares: {soma}\nMultiplicação dos ímpares: {multi}")

print("fim")
