import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")

    # Estrutura: inicialização das variáveis utilizadas no jogo
    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    # Estrutura: o nível é uma variável intermediária para definir o total
    nivel = int(input("Define o nível de dificuldade: "))

    if (nivel == 1):
        total_tentativas = 6
    elif (nivel == 2):
        total_tentativas = 4
    else:
        total_tentativas = 2

    # Estrutura: laço
    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        # Estrutura: condições
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        # Estrutura: conclusão do teste
        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

                    # A variável rodada já está definido através do 'for', assim como o incremento já é feito pelo for,
                    # diferente do while:
                    # rodada = rodada + 1

                    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
