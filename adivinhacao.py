print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 47
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}". format(rodada, total_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    # A variável rodada já está definido através do 'for', assim como o incremento já é feito pelo for,
    # diferente do while:
    # rodada = rodada + 1

    print("Fim do jogo")
