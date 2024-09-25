def criarL(lista,n):
    for i in range(n):
        elem = int(input("elemento da lista: "))
        lista.append(elem)

def lerL(lista):
    for i in range(len(lista)):
        print(f" {lista[i]} ,",end='')
    print(" FIM")

def interL(lista1,lista2):
    y = len(lista1)
    L= []
    for i in range(y):
        for j in range(y):
            if lista1[i] == lista2[j]:
                elem = lista1[i]
                L.append(elem)
    return L

num = int(input("quantos elementos tera as listas: "))

L1 = []
L2 = []

criarL(L1,num)
criarL(L2,num)

L3 = interL(L1,L2)

lerL(L3)
