# # Lista: representa uma sequencia de valores

# n1 = [1,5,3,5,3]
# n2 = [5,2,4,7,4,2,4]

# valores = n1 + n2

# valores[0] = 9

# print(12 in valores)

# planetas = ['mercurio', 'venus', 'marte','saturno', 'urano', 'netuno']
# for planeta in planetas: 
#     print(planeta)

bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita')

    bebida = input()

    bebidas.append(bebida)

bebidas.sort()

print(f'Bebidas escolhidas:')

for bebida in bebidas: 
    print(bebida)

print(f'Saude!')