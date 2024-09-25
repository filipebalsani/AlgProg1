c = int(input("capacidade da cabine: "))
a = int(input("numero de alunos: "))
v = 0

while a > 0:
    d = c-1
    a = a - d
    v = v + 1
print(v)

