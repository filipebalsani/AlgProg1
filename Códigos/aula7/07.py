nome = input("Nome: ")

up = nome.upper()

for i in range(len(nome)+1):
    if i != 0:
        print(up[-i],end='')
