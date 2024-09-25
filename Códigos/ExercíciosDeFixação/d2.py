
p = int(input("P:"))
d1 = int(input("D_1:"))
d2 = int(input("D_2:"))

# se p = 0 (A = par, B = ímpar) ; se p = 1 (A = ímpar, B = par)

if p == 0 or p == 1:
    if d1 < 0 or d1 > 5 or d2 < 0 or d2 > 5 :
        print("Valor D inválido")
    else:
        r = (d1+d2) % 2
        if p != r: # pela tabela verdade quando p é diferente de r Bob vence
            print("1")
        else:       # e quando p é igual a r Alice vence
            print("0")
    
else:
    print("Valor P inválido")

