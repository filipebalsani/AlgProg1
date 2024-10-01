st = input("String: ")
l = len(st)

palind = True

i = 0
f = l - 1
stop = l/2


while palind and i < stop:
    if st[i] != st[f]:
        palind = False

    i += 1
    f -= 1
        

if palind:
    print("A string eh palíndromo.")
else:
    print("A string NAO eh palíndromo.")
