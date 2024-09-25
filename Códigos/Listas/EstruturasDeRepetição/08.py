c = -1
n = 0
p = 0
x = 1
s = 0

while x != 0:
    x = int(input("Digite um valor(para encerrar digite 0): "))
    c = c + 1
    print(c)
    s = s + x
    if x > 0:
        p = p + 1
    elif x < 0:
        n = n + 1
m = float(s / c)
p5 = float(p/c)*100
n5 = float(n/c)*100
print(f"Média = {m} ; quantidade de valores positivos: {p} (em porcentagem: {'%.2f' % p5}%)")
print(f"quantidade de valores negativos: {n} (em porcentagem: {'%.2f' % n5}%)")
