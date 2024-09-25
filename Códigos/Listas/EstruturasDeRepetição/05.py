n = int(input("Número de termos: "))
a = int(input("Primeiro termo: "))
r = int(input("Razão da progressão: "))
i = 0
s = 0
print(f"S = {a} ",end='')

while i < n-1:
    s = s + a
    a = a + r
    i = i + 1
    print(f"+ {a} ", end='')
s = s + a
print(f"\nS = {s}")

