frase = "Eu posso ajudar respondendo perguntas no fórum!"
sorteio = [5, -4, 3, -8, 11]
acertos = 0
for i in sorteio:
    resposta = input("Qual o caractere de índice %d?" %(i))
    if frase[i] == resposta:
        print("Parabéns, você acertou!")
        acertos += 1
    else:
        print("Você errou. O caractere de índice %d é: %s"%(i,frase[i]))
print("Você acertou %d de %d perguntas."%(acertos, len(sorteio)))
