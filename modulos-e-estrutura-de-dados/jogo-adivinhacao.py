import random
import os

novo_jogo = 's'

tentativas = 3

while novo_jogo == 's':
    print(f'Bem vindo ao jogo!')
    print(f'Voce tera 3 chances para adivinhar um numero entre 1 e 15!')

    #gerar o numero aleatorio secreto

    num = random.randint(1,15)

    #jogar

    for i in range(3):
        print(f'Qual o seu chute?')
        chute = int(input())
        if chute == num:
            print(f'Parabens, voce ganhou!')
            break
        elif chute > num:
            print(f'Chute um numero mais baixo.')
        else:
            print(f'Chute um numero mais alto!')

    # Caso não acerte, revelar o chute

    if chute !=  num: 
        print(f'Que pena, voce perdeu. o numero secreto era {num}')

    novo_jogo = input(f'Deseja jogar outra vez? s para sim, outra tecla para nao:')

    novo_jogo = novo_jogo.lower()

    # limpar a tela

    os.system('cls')