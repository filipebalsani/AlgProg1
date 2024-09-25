f = 0
x = 0
n = 1
c = 0
while c < 11:
    print(f, end ='')
    print(", ", end='')
    x = f
    f = x + n
    n = x 
    c = c + 1
print("...")
