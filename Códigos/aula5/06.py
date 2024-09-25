

matA = []
matB = []
matC = []

# a = nxm b = mxp
n = int(input("numero de linhas de A? "))

m = int(input("numero de colunas de A? "))

p = int(input("numero de colunas de B? "))

for i in range(n):
    linha = []
    for j in range(m):
        elem = int(input(f"A: {i} {j}: "))
        linha.append(elem)
    matA.append(linha)
ln = 0
cn = 0

for i in range(m):
    linha = []
    for j in range(p):
        elem = int(input(f"B: {i} {j}: "))
        linha.append(elem)
    matB.append(linha)
ln = 0
cn = 0

# matriz C = A*B
for i in range(n):
    linha = []
    for j in range(p):
        # for a colunas
        elem = 0
        for k in range(m):
            elem += matA[i][k] * matB[k][j]
        linha.append(elem)
    matC.append(linha)
    
# a linhas = n / a colunas = m / b linhas = m / b colunas = p
# C(00) = A(00) * B(00) + A(01) * B(10)
# C(01) = A(00) * B(01) + A(01) * B(11)
# C(02) = A(00) * B(02) + A(01) * B(12)
# C(10) = A(10)*B()+A()*B()

for i in range(n):
    for j in range(p):
        print(f"{matC[i][j]} ", end="")
    print(".")

print(f"FIM")
            
        
