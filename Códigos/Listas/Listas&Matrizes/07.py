import random

mata = []

matb = []


for i in range(3):
    linha = []
    for j in range(4):
        elem = random.randint(0,100)
        linha.append(elem)
    mata.append(linha)


for i in range(3):
    linha = []
    for j in range(4):
        elem = random.randint(0,100)
        linha.append(elem)
    matb.append(linha)

iguais = []

for i in range(3):
    for j in range(4):
        for k in range(3):
            for l in range(4):
                A = mata[i][j]
                B = matb[k][l]
                if A == B:
                    elem = mata[i][j]
                    iguais.append(elem)

print("MATRIZ A:\n")

for i in range(3):
    for j in range(4):
        print(f"{mata[i][j]} ",end='')
    print("\n",end='')


print("\nMATRIZ B:\n")

for i in range(3):
    for j in range(4):
        print(f"{matb[i][j]} ",end='')
    print("\n",end='')


print("\nNumeros iguais: ")
for i in range(len(iguais)):
    print(f"{iguais[i]} ",end='')
