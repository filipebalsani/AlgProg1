mat = []

n = int(input("quant linhas? "))

m = int(input("quant colunas? "))


for i in range(n):
    linha = []
    for j in range(m):
        elem = int(input(f"{i} {j}: "))
        linha.append(elem)
    mat.append(linha)
ln = 0
cn = 0

for i in range(n):
    count = 0
    for j in range(m):
        if mat[i][j] == 0:
            count+=1
    if count == m:
        ln +=1

for j in range(m):
    count = 0
    for i in range(n):
        if mat[i][j] == 0:
            count+=1
    if count == n:
        cn +=1
print(f"Linhas nulas: {ln}")
print(f"Colunas nulas: {cn}")
            
        
