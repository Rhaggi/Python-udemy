# forçar uma exceção

from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass

# colocar em um while

# if __name__ == '__main__':
#     try:
#         num = int(input('Digite um numero positivo:'))
#         if num < 0:
#             raise NumeroNegativoError
#     except NumeroNegativoError:
#         print(f'Foi fornecido um numero negativo!')
#     else:
#         print(f'A raiz quadrada de {num} é {sqrt(num)}')
#     finally:
#         print(f'Fim do cálculo')

# Como exercicio, colocar o codigo acima dentro de um while

while True:
    try:
        num = int(input('Digite um numero positivo:'))
        if num < 0:
            raise NumeroNegativoError
    except NumeroNegativoError:
        print(f'Foi fornecido um numero negativo!')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
        break
    finally:
        print(f'Fim do cálculo')