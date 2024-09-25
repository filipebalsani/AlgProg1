mat = []
n = int(input("quantas linhas? "))
m = int(input("quantas colunas? "))


for i in range(n):
    linha = []
    for j in range(m):
        elem = int(input(f"elem linha {i}: "))
        linha.append(elem)
    mat.append(linha)

big = [0][0]
small = mat[0][0]

for i in range(n):
    for j in range(m):
        if mat[i][j] > big:
            big = mat[i][j]
        if mat[i][j] < small:
            small = mat[i][j]
        print(f"{mat[i][j]} ", end="")
    print(".")

print(f"Maior elemento da matriz: {big}")
print(f"Menor elemento da matriz: {small}")
