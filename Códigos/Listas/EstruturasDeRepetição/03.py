t = 0
m = 0
i = 0

while i < 5:
    p1 = int(input(f"nota P1 do aluno {i+1}: "))
    p2 = int(input(f"nota P2 do aluno {i+1}: "))
    p3 = int(input(f"nota P3 do aluno {i+1}: "))
    m = float((p1*2 + p2*3 + p3*4) / 9)
    t = t + m
    print(f"Aluno {i+1}: Média = {'%.2f' % m} ; ", end='')
    if m >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
    i = i + 1
t = float(t/5)
print(f"Média da turma = {'%.2f' % t}")
