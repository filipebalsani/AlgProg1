c = int(input("quantidade de competidores:"))
p = int(input("quantidade de folhas de papel especial:"))
f = int(input("quantidade de folhas que cada competidor deve receber:"))

r = p / c

if r >= f:
    print("S")
else:
    print("N")
        
