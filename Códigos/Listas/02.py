s = 0
i = 2
c = 0
t = 0
while t < 20:
    j = 2
    c = 0
    while j < i+1:
        if i%j == 0:
            c = c + 1
        j = j + 1
    if c == 1:
        print(f"{i}, ",end='')
        t = t + 1
    i = i + 1

print("FIM")
