# 1. Dada a lista de tuplas, remova todas as tuplas com comprimento K. O programa 
# deverá ler o valor de K com o usuário via teclado. A lista de entrada será sempre a 
# mesma do exemplo abaixo (ou seja, test_list):

# test_list = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]

# tamanho_excluir = int(input(f'Digite um numero: '))

# resultado = [r for r in test_list if len(r) != tamanho_excluir]

# print(resultado)

# 2 -Crie uma lista com 10 números inteiros e:

# Exiba o maior e o menor número.
# Calcule a soma e a média dos números.

# list = [2,1,5,7,9,5,3,7,98,43]
# media = sum(list)/len(list)

# print(max(list))
# print(sum(list))
# print(media)

# 3 - Dada a lista ["maçã", "banana", "laranja", "uva"]:

# Adicione “melancia” ao final.
# Remova “banana”.
# Ordene a lista em ordem alfabética.

# frutas = ["maçã", "banana", "laranja", "uva"]

# frutas.append('melancia')

# print(frutas)

# frutas.remove('banana')

# print(frutas)


# print(sorted(frutas))

# 4 - Crie uma lista com números de 1 a 20 e:

# Gere uma nova lista apenas com números pares.
# Inverta a ordem da lista original.

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(num)

n_pares = []

for numero in num:
    if numero % 2 == 0:
        n_pares.append(numero)

print(n_pares)

num.reverse()

print(num)