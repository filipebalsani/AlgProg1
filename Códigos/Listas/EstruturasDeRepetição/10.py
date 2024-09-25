
pi = float(4)
i = 1
while i < 320000:
    d = 1 + 2*i
    if i % 2 == 0:
        pi = pi + float(4/d)
    else:
        pi = pi - float(4/d)
    i = i + 1
print(f"{'%.6f' % pi}")
#print(f"3.14159 -> {'%.6f' % pi} {pi} FIM")
#3,14159 26535
