L=[]
L1=[] # sem elementos repitidos
L2=[] # apenas elementos que se repetem


stop = True

n = int(input("Quantos numeros tera na lista? "))
i=0

while i<n:
    numero = int(input("add num to list: "))
    
    if numero == -1:
        stop = False
    else:
        L.append(numero)
    i+=1
    
i = 0

while i < len(L):

    j = i+1
    igual = False
    
    while j < len(L):
        if L[i] == L[j]:
            igual = True
        j += 1

    if igual:
        L2.append(L[i])
    else:
        L1.append(L[i])

        
    i += 1

print(f"LISTA ORIGINAL: {L}")
print(f"LISTA s/ REPETIÇÕES: {L1}")
print(f"LISTA dos ELEMENTOS que repetem: {L2}")


print("fim")
