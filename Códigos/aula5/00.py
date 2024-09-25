matriz = [[1,2], [3,4], [5,6], [7,8]]
i=0
while i < len(matriz):
    print(f"Elementos da linha {i}")
    j=0
    while j < len(matriz[i]):
        print(f"{matriz[i][j]}")
        j += 1
    i +=1
