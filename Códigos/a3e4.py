x = 1
y = 1

while x < 11:
    while y < 11:
        print(f"| {x} x {y} = {y*x} ", end='')
        y = y +1
    print("|")
    x = x + 1
    y = 1
