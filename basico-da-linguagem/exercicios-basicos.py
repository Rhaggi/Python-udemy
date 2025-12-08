# exercicio 01

# from datetime import datetime

# ano_nascimento = int(input('Digite o ano que voce nasceu: '))

# ano_atual = datetime.now().year

# idade = ano_atual - ano_nascimento

# print(f"Voce tem ou fará {idade} anos.")

# exercicio 02 - verificar par ou impar

# numero = int(input('Digite um numero: '))

# if numero % 2 == 0: 
#     print('O numero é par')
# else:
#     print('O numero é impar')

# exercicio 3 - Gere a tabuada de um número escolhido pelo usuário.

# numero = int(input('Digite um numero para saber sua tabuada: '))
# multiplicador = 1

# for mult in range(10):
#     conta = numero * multiplicador
#     print(conta)
#     multiplicador = multiplicador + 1

# exercicio 4 - Jogo de Adivinhação

import random

venceu = False 
num_aleatorio = random.randint(1,50)
tentativas = 0

while(venceu != True):

    usuario = int(input('Adivinhe o numero entre 1 e 50: '))
    tentativas = tentativas + 1
    
    if (tentativas == 3):
        print('Que pena, voce perdeu.')
        break
    elif(usuario == num_aleatorio):
        print('Parabens, voce acertou!')
        venceu = True
    elif (usuario < num_aleatorio):
        print('Chute um numero mais alto!')
    elif ( usuario > num_aleatorio): 
        print('Chute um numero mais baixo!')