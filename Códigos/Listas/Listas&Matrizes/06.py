mat=[]
matf=[]
m=10
n=20

for i in range(m):
    linha = []
    for j in range(n):
        elem=int(input(f"{i} {j}: "))
        linha.append(elem)
    mat.append(linha)

lsoma = []


for i in range(m):
    soma = 0
    for j in range(n):
        soma += mat[i][j]
    lsoma.append(soma)

for i in range(m):
    linha = []
    for j in range(n):
        elem = mat[i][j] * lsoma[i]
        linha.append(elem)
    matf.append(linha)

print("Matriz inicial:")

for i in range(m):
    for j in range(n):
        print(f"{mat[i][j]} ",end='')
    print("\n",end='')

print("\nMatriz final:")


for i in range(m):
    for j in range(n):
        print(f"{matf[i][j]} ",end='')
    print("\n",end='')

    
