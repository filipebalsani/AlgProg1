gasto = float(input("Quanto o cliente gastou:"))

if gasto <= 100:
    print(gasto*0.95)
elif gasto < 200:
    print(gasto*0.9)
else:
    print(gasto*0.8)
