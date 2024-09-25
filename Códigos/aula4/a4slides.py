L = [] #lista vazia (open valores [string, numero])
# L[-1] acessa o último elemento, -2 o penultimo e assim por diante
# print(L) imprime todos os elmentos da lista
# 'maçã' in frutas = true or false
# len(L) = numero de elementos da lista (len = x ; n de ele = x+1)
# operador + concatena listas
# L = L + ["string"]
# L.append("string")
# toda lista tem um id ( print(id(L)) )
# a função append() não muda o id da lista, mas
# a operação L = L + ["string"] muda o id da lista
# função insert(1, 'string') adiciona um elemento em uma posição especifica
# o comando del remove um elemento da lista
# del L[2]
# operador # repete os itens em uma lista:
# print([1, "ola" * 2]) = [1, ola, ola]
# operação de fatiar: [1,2,3,4,5,6] print(L[2(i):4(n/i)]) = 3,4
# print(L[:]) = 1,2,3,4,5,6
# L[4:4] = [7,8] :-> = 1,2,3,4,7,8,5,6
# L[1:3} = ['x', 'y']
# L[1:3] = []   remove x e y
# del L[1:4]    remove ele 1,2,3
# cirar lista de inteiros consecutivos: L = list(range(5,13)) = [5, ..., 12]
# caso haja 3 agrunmentos: L=list(range(2,23,3)) = 2,5,8,11,14,17,20

i = 0
while i < 10:
    numero = int(input(f"{i+1} numero: "))
    L.append(numero)
    i += 1

i=0

soma = 0

print("ímapres: ", end='')

while i < 10:
    if L[i] % 2 != 0:
        print(f"{L[i]} , ", end='')
    soma += L[i]
    i+=1

maior = L[0]
menor = L[0]

i = 1

while i < 10:
    if L[i] > maior:
        maior = L[i]
    if L[i] < menor:
        menor = L [i]
    i+=1
print(f"\nmaior elemento = {maior}")
print(f"menor elemento = {menor}")
print(f"soma dos elementos = {soma}")
print("elementos maiores de 18: ",end='')

i = 0

while i < 10:
    if L[i] > 18:
        print(f"{L[i]} , ",end='')
    i+=1

print("\nfim")
