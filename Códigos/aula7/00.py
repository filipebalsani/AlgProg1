frase = ''
frase = frase + "Essa string usa "
meio = '"apóstrofes" '
fim = "como demarcador. "
frase = frase+meio+fim

fatia1 = frase[:10]
fatia2 = frase[-10:]

print("A frase: ", frase)
print("Fatia 1: ", fatia1)
print("Fatia 2: ", fatia2)
print("Tem comprimento: ", len(fatia2))

texto = "esse texto eh uma string"
print(texto)
#texto[2] = 'S' # erro
print(texto)

a,b,c,d,e = "Hello"

print(a)
print(b)
print(c)
print(d)
print(e)
