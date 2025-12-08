# é um objeto que representa um erro durante a execução do programa

# blocos try.... except

def div(a,b):
    return round(a/b, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input(f'Digite um numero:'))
            n2 = int(input(f'Digite outro numero:'))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor, tente novamente')

    try:
        r = div(n1,n2)
    except ZeroDivisionError:
        print(f'Não é possivel dividir por 0')
    except:
        print(f'Ocorreu um erro desconhecido')
    else: 
        print(f'Resultado: {r}')
    finally:
        print(f'Fim do cálculo')




