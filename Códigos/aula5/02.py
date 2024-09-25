mat = []
n = int(input("dimensão da matriz quadrada: "))

for i in range(n):
    linha = []
    for j in range(n):
        elem = int(input(f"linha {i}: "))
        linha.append(elem)
    mat.append(linha)

sim = True

for i in range(n):
    for j in range(n):
        if i != j:
            if mat[i][j] != mat[j][i]:
                sim = False

if sim:
    print("é simetrica")
else:
    print("NAO é simetrica")

