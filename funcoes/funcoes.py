# Promove o reuso de codigo e a legibilidade; existem as funçoes internas e as criadas por nós

# def de define
# def nome_funcao ([argumento])
#     <instruçoes>

# def mensagem():
#     print('Bóson treinamentos em tecnologia')
#     print('CURSO COMPLETO EM PYTHON')

# mensagem()

# FUNÇÃO COM ARGUMENTOS 

# def soma(a,b):
#     print(a + b)

# soma(12, 7)

# def mult(x, y):
#     return x*y

# a = 5
# b = 2
# c = mult(a,b)

# print(f'A multiplicação de {a} e {b} é {c}')

# def div(k,j): 
#     if j != 0:
#       return k/j
#     else:
#         return 'Impossivel dividir por 0'

# if __name__ == '__main__':
#     a = int(input(f'Digite um numero:'))
#     b = int(input(f'Digite outro numero:'))

#     r = div(a,b)

#     print(f'{a} dividido por {b} é igual a {r}')

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados

# def contar(caractere, num=11):
#     for n in range(1, num):
#         print(caractere)

x = 5
y = 6
z = 3

def soma_mult(a,b,c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c

if __name__ == '__main__':
    res = soma_mult(x,y,z)
    print(res)