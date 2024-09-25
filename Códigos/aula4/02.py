L=[]

stop = True

while stop:
    numero = int(input("add num to list (-1 to stop): "))
    if numero == -1:
        stop = False
    else:
        L.append(numero)
i = 0
soma = 0
while i < len(L):
    print(f"{L[i]} , ",end='')
    soma += L[i]
    i+=1
    
media = soma / len(L)
print(f"\nMedia = {media}")
print("fim")
