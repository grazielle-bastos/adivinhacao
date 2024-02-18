import random

print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_tentativas = 3

print(numero_secreto)

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}". format(rodada, total_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    # A variável rodada já está definido através do 'for', assim como o incremento já é feito pelo for,
    # diferente do while:
    # rodada = rodada + 1

    print("Fim do jogo")
