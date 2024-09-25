
pi = float(4)
i = 1
t = 100
f = 1
n = float(t/1)
while i < 20:
    f = f * i
    n = float(n + (t-i)/f)
    i = i + 1
print(n)
