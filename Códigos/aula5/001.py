mat = []
n = int(input("Quantas linhas na matriz? "))

m = int(input("Quantas colunas na matriz? "))
for i in range(n):
    linha = []
    print(f"Informe os elementos da linha {i}: ")
    for j in range(m):
        elem = int(input("Entre com o elemento da coluna {j}: "))
        linha.append(elem)
    mat.append(linha)
for i in range(n):
    for j in range(m):
        print(f"{mat[i][j]} ", end="")
    print(".")
