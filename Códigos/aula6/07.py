def criarL(lista,n):
    for i in range(n):
        elem = int(input("elemento da lista: "))
        lista.append(elem)

def lerL(lista):
    for i in range(len(lista)):
        print(f" {lista[i]} ,",end='')
    print(" FIM")

def uniaoL(lista1,lista2):
    L = []
    y = len(lista1)
    for i in range(y):
        elem = lista1[i]
        L.append(elem)

    
    
    for i in range(y):
        enc = False
        for j in range(y):
            if lista2[i] == L[j]:
                enc = True
        if enc == False:
            elem = lista2[i]
            L.append(elem)

    return L

num = int(input("Quantos elementos tera a lista: "))

L1 = []
L2 = []

criarL(L1,num)
criarL(L2,num)

L3 = uniaoL(L1,L2)

lerL(L3)
