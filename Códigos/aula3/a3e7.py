n = 0
x = 0
m = 0
gt6 = 0
gt4 = 0
lt4 = 0
while x > -1:
    x = float(input("Valor: "))
    n = n + 1
    if x > -1:
        m = (m+x) / n
        if x < 4:
            lt4 = lt4+1
        elif x < 6:
            gt4=gt4+1
        else:
            gt6=gt6+1


print(f"{gt6} notas maior ou igual a 6")
print(f"{gt4} notas maior ou igual a 4 e menor que 6")
print(f"{lt4} notas menor que 4")
print(f"Média = {m}")
