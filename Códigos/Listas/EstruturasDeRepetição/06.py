n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
t = 0
i = 2
m1 = 1
m2 = 1

if n2 > n1:
    t = n2
    n2 = n1
    n1 = t

while n1 * i % n2 != 0:
    i = i + 1
print(i*n1)
