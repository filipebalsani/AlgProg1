mat = []
n = int(input("dimensão da matriz quadrada: "))

trans = []

num = []
bol = []

for i in range(n):
    linha = []
    for j in range(n):
        x = i*3+j
        y = True
        bol.append(y)
        num.append(x)
        elem = int(input(f"linha {i}: "))
        linha.append(elem)
    mat.append(linha)
trans.append(num)
trans.append(bol)

for i in range(n):
    for j in range(n):
        if i != j and  trans[1][i*3+j]:
            trans[1][i*3+j] = False
            trans[1][j*3+i] = False
            temp = mat[i][j]
            print(mat[i][j])
            print(mat[j][i])
            mat[i][j] = mat[j][i]
            mat[j][i] = temp



for i in range(n):
    for j in range(n):
        print(f"{mat[i][j]} ", end="")
    print(".")



