mat = []
n = int(input("ordem da matriz: "))

for i in range(n):
    linha = []
    
    for j in range(n):
        elem = int(input(f"linha {i} c {j}: "))
        linha.append(elem)
    mat.append(linha)

id = True

for i in range(n):
    for j in range(n):
        if i == j and mat[i][j] != 1:
            id = False
        if i != j and mat[i][j] != 0:
            id = False
if id:
    print("matriz é identidade")
else:
    print("matriz NAO é identidade")
