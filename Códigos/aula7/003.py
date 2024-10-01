texto = "Esse é um 'string'"
print(texto)
novo_texto = 'Mais' + texto[6:]
print(novo_texto)

ss = "Hello, World"
print(ss.upper())
tt = ss.replace("o", "***")
print(tt)

food = "banana bread"

print("*"+food.center(25)+"*")
print("*"+food.ljust(25)+"*")
print("*"+food.rjust(25)+"*")

print(food.find("e"))
print(food.find("na"))
print(food.find("b"))


print(food.rfind("e"))
print(food.rfind("na"))
print(food.rfind("b"))


print(food.index("e"))
