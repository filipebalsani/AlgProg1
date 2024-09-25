mat = []

for i in range(3):
    linha = []
    for j in range(3):
        elem = int(input("elem: "))
        linha.append(elem)
    mat.append(linha)

sl = []
sd = []
d = 0
for i in range(3):
    s = 0 #soma linha
    for j in range(3):
        if i == j:
            d += mat[i][j]
        s += mat[i][j]
    sl.append(s)

sd.append(d)


ele = 0
ele = mat[2][0]+mat[1][1]+mat[0][2]

sd.append(ele)

sc = []

for i in range(3):
    s = 0 #soma linha
    for j in range(3):
        s += mat[j][i]
    sc.append(s)

for i in range(3):
    for j in range(3):
        print(f"{mat[i][j]}  ", end ='')
    print("\n",end='')

magico = True

for i in range(3):
    #print(f"linha: {sl[i]} coluna: {sc[i]}")
    if sl[i] != ele or sc[i] != ele:
        magico = False
for i in range(2):
    #print(f"diagonal: {sd[i]}")
    
    if sd[i] != ele:
        magico = False

if magico:
    print("É Mágico!")
else:
    print("Não é Magico :/")



print("\nfim")
            
