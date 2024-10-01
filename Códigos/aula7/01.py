string = input("String: ")
char = input("Letra: ")
j = string.find(char)
r = string[:j] + string[j+1:]
print(r)

