import tkinter as tk
import random
def JogarPedra():
    print("Jogador escolheu Pedra")
    computador = random.randint(0,2)
    JogadaComputador = ListaJogadas[computador]
    if(JogadaComputador == "Papel"):
        print("Computador escolheu Papel")
        print("Computador Ganhou")
    elif(JogadaComputador == 'Tesoura'):
        print("Computador escolheu Tesoura")
        print("Jogador Ganhou")
    else:
        print("Computador escolheu Pedra")
        print("Empatou")
def JogarPapel():
    print("Jogador escolheu Papel")
    computador = random.randint(0,2)
    JogadaComputador = ListaJogada[computador]
    if(JogadaComputador):
        print("Computador escolheu Papel")
        print("Empatou")
    elif(JogadaComputador == 'Tesoura'):
        print("Computador escolheu Tesoura")
        print("Computador Ganhou")
    else:
        print("Computador escolheu Pedra")
        print("Jogador Ganhou")
def JogarTesoura():
    print("Jogador escolheu Tesoura")
    computador = random.randint(0,2)
    JogadaComputador = ListaJogada[computador]
    if(JogadaComputador == "Papel"):
        print("Computador escolheu Papel")
        print("Jogador Ganhou")
    elif(JogadaComputador == 'Tesoura'):
        print("Computador escolheu Tesoura")
        print("Empatou")
    else:
        print("Computador escolheu Pedra")
        print("Computador Ganhou!")
janela = tk.Tk()
janela.title("Pedra, Papel ou Tesoura")
janela.geometry("900x600")
botaoPedra = tk.Button(janela, text="Pedra", command=lambda:jogarPedra())
botaoPedra.place(x=50, y=50)
botaoPapel = tk.Button(janela, text="Papel", command=lambda:jogarPapel())
botaoPapel.place(x=250, y=50)
botaoTesoura = tk.Button(janela, text="Tesoura", command=lambda:jogarTesoura())
botaoTesoura.place(x=450, y=50)
listaJogadas = ["Pedra", "Papel", "Tesoura"]
janela.mainloop()