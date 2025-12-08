# Criar um programa de cálculo de raizes de equações de segundo grau

# equação: ax^2 + bx + c = 0

import sys
import os

def raizes(a, b, c):
    d = (b**2 - 4*a*c)
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)

    print(f'\nValor de x1: {x1: .2f}')
    print(f'\nValor de x1: {x2: .2f}')

    # opcional: retornar os valores em uma lista

    valores = []

    valores.append(x1)
    valores.append(x2)

    return valores

if __name__ == '__main__':
    while True:
        print(f'Calcular as raizes de uma equação de segundo grau\n')
        print(f'Equação no formato ax2 + bx + c = 0\n')

        try:
            a = float(input(f'Entre com o valor de A: '))
            b = float(input(f'Entre com o valor de B '))
            c = float(input(f'Entre com o valor de C: '))
        except ValueError:
            print(f'Digite somente numeros!')
        else:
            res = raizes(a,b,c)
            print(res)

        while True:
            continua = input(f'\nDigite q para sair ou n para novo cálculo: ')

            if(continua.lower() == 'q'):
                sys.exit()
            elif (continua.lower() == 'n'):
                os.system('cls')
                break
            else:
                print(f'Entrada inválida')



