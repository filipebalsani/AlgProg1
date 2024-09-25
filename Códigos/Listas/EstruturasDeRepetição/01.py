s = 0
i = 1

while i < 501:
    if i%2 == 1 and i%3 == 0:
        s = s + i
    i = i + 1
print(s)
