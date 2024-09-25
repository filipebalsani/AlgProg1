n1 = int(input("digite o 1o numero:"))
n2 = int(input("digite o 2o numero:"))
n3 = int(input("digite o 3o numero:"))
n4 = int(input("digite o 4o numero:"))
n5 = int(input("digite o 5o numero:"))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5



print(f"o maior numero é {maior}")
