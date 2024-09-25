L = []
n = int(input("tamanho da lista: "))
i = 0
while i < n:
    nome = input(f"{i+1} nome: ")
    L.append(nome)
    i += 1
i = 0
while i < n:
    print(f"{i+1} = {L[i]}")
    i += 1
nome = input("Qual nome deseja procurar na lista? ")
i = 0
bool = 0
achou = False
while bool == 0 and  i < n and not achou:
    if L[i] == nome:
        print(f"O nome {nome} esta na lista.")
        bool = 1
        achou = True
    i+=1
    if i == n and bool == 0:
        print(f"O nome {nome} não esta na lista.")

