string = input("String: ")
char = input("Letra: ")
teste = "isso eh um tehste"
j = teste.find(char)
# teste[n1(include) : n2(not include)]
r = teste[:j] + teste[j+1:]
print(r)

j = teste.find(char)
r = teste[:j] + teste[j+1:]
print(r)

