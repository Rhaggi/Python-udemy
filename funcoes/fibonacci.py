# Desafio Fibonacci - Crie um programa que retorne a sequencia fibonacci com quantos numeros o usuario desejar.
# ex: o usuario quer 5 numeros: 0, 1, 1, 2, 3.

# Caso base: fibonacci(num), se num <= 1
# Caso recursivo: fibonacci(num-1) + fibonacci(num -2), para num > 1

def fibonacci(num):
    if num == 1:
        return[0]
    elif num == 2:
        return[0,1]
    else:
        sequencia = fibonacci(num-1)
        sequencia.append(sequencia[-1] + sequencia[-2])
        return sequencia
    

if __name__ == '__main__': 
    x = int(input(f'Digite quantos numeros da sequencia você quer: '))
    try:
        res = fibonacci(x)
    except RecursionError:
        print('O numero fornecido é muito grande ou negativo')
    else:
        print(f'\nA sequencia de fibonacci com {x} elementos é {res}')