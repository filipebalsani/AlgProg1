st1 = input("string 1: ")
st2 = input("string 2: ")
up1 = st1.upper()
up2 = st2.upper()

comp1 = len(st1)
comp2 = len(st2)

anagrama = True


i = 0
while anagrama and i < comp1:
    if up1[i] != " ":
        x = 0
        for j in range(comp1):
            if up1[j] == up1[i]:
                x += 1
        y = 0
        for k in range(comp2):
            if up2[k] == up1[i]:
                y += 1
        if x != y:
            anagrama = False
    i += 1



if anagrama:
    print("É anagrama")
else:
    print("NÃO é anagrama")
