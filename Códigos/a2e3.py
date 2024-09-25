n1 = int(input("Digite o 1o numero:"))
n2 = int(input("Digite o 2o numero:"))
n3 = int(input("Digite o 3o numero:"))

maior = 0
menor = 0
meio = 0

if n1 > n2: # n2 MAIOR  n1 menor
    maior = n1
    menor = n2
    if n3 > maior:
        maior = n3
        meio = n1
    else:
        if n3 < menor:
            menor = n3
            meio = n2
        else: meio = n3
else:   #   n1 MAIOR  n2 menor
    maior = n2
    menor = n1
    if n3 > maior:
        maior = n3
        meio = n2
    else:
        if n3 < menor:
            menor = n3
            meio = n1
        else: meio = n3
print("Em ordem crescente:",menor,meio,maior)
'''
1 2 3   
1 3 2   
2 3 1

2 1 3   
3 1 2   
3 2 1   

'''
