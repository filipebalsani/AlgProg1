idade = int(input("Digite sua idade:"))

if idade < 16:
    print("Você não tem idade para votar")
elif idade < 18:
    print("Seu voto é facultativo")
elif idade < 66:
    print("Seu voto é obrigatório")
else: print("Você está dispensado de votar")
