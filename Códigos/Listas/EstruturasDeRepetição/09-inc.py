n = 0
c = 0
k = 1

while c < 4:
    i = 1
    s = 0
    #print(k)
    while i < k:
        
        if k % i == 0:
            #print(f"{k} é div por {i}")
            s = s + i
        i = i + 1
    #print(k, i, s)
    #print(f"soma de {k} = {s}")
    if k == s:
        c = c + 1
        print(f"count: {c} ; numero: {k}")
    k = k + 1
print(8191*4096)

'''
formula dos numeros perfeitos:
soma das potencias de 2:
1+2+4+8+16 ... + 4096
vezes a potencia de 2:
(1+2 = 3) * 2 = 6
(1+2+4 = 7) * 4 = 28
(1+2+4+8+16 = 31) * 16 = 496
porem a soma tem que dar um numero primo:
(1+2+4+8 = 15) * 8 = 120 (não funciona pq 15 não é primo)
