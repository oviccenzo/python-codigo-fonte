# forca.py

import random
from abc import abstractclassmethod


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    #palavra_secreta = carrega_palavra_secreta("frutas.txt")

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    acertou = False
    enforcou = False

    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if ((chute in palavra_secreta) and (chute not in letras_acertadas)):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7

        acertou = "_" not in letras_acertadas

        letras_faltando = (letras_acertadas.count("_"))

        print(letras_acertadas)
        print("Ainda faltam acertar {} letras. Você ainda tem {} palpites.".format(letras_faltando, 7 - erros))

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra.upper() == chute.upper()):
            letras_acertadas[index] = letra

        index += 1


def pede_chute():
    chute = input("Digite uma letra?  ")
    chute = chute.strip().upper()
    return chute


def carrega_palavra_secreta(nome_arquivo = "palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha.upper())

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    return palavras[numero]

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {} \n".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
