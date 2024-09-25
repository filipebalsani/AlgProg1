mat = []

m = 4
n = 5



for i in range(m):
    linha = []
    for j in range(n):
        ele = int(input(f"{i} {j}: "))
        linha.append(ele)
    mat.append(linha)

linm = 0
min = mat[0][0]

for i in range(m):
    for j in range(n):
        if mat[i][j] < min:
            min = mat[i][j]
            linm = i
max = mat[linm][4]
colm = 4
for i in range(n):
    if mat[linm][i] > max:
        max = mat[linm][i]
        print(i)
        colm = i


for i in range(m):
    for j in range(n):
        print(f" {mat[i][j]} ",end='')
    print("\n",end='')
print(f"\nMaior elemento: {max}  posição: ({linm}),({colm})")

print("fim")
        
