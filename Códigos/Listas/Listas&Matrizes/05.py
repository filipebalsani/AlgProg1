mat = []
maior = []
menor = []

n=7

for i in range(n):
    linha = []
    for j in range(n):
        elem = int(input(f"{i} {j}: "))
        linha.append(elem)
    mat.append(linha)


for i in range(n):
    big = mat[i][0]
    small = big
    for j in range(n):
        if mat[i][j] > big:
            big = mat[i][j]
        if mat[i][j] < small:
            small = mat[i][j]
    maior.append(big)
    menor.append(small)

for i in range(n):
    for j in range(n):
        print(f" {mat[i][j]} ",end='')
    print("\n",end='')

print("\nLista dos maiores: ", end='')
for i in range(7):
    print(f"{maior[i]} ",end='')
print("\nLista dos menores: ",end='')
for i in range(7):
    print(f"{menor[i]} ",end='')

print("fim")
        
