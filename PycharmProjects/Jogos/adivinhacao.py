#adivinhacao.py
import random

def jogar() :

    print("***************************************")
    print("*  Bem vindo ao jogo de Adivinhação!  *")
    print("***************************************")

    print("Qual o nível você quer jogar? ")
    print("(1) Fácil    (2) Médio   (3) Difícil ")

    nivel = int(input("Defina o nível: "))
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite seu número secreto: "))
        print("Voce digitou: ", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        else:
            acertou = numero_secreto == chute
            maior = chute > numero_secreto
            menor = chute < numero_secreto
            if (acertou):
                print("Voce acertou!!! E fez {} pontos".format(pontos))
                break
            else:
                if (maior):
                    print("Voce errou!!! O seu chute foi maior que o número secreto.")
                elif (menor):
                    print("Voce errou!!! O seu chute foi menor que o número secreto.")
            pontos_perdidos = numero_secreto - chute
            pontos = abs(pontos_perdidos - pontos)

    print("Fim do jogo!!!")

if (__name__ == "__main__"):
    jogar()
