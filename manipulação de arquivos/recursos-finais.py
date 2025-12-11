# Trocar valores entre duas variaveis

var1 = 12
var2 = 31

# var2, var1 = var1, var2

# print(f'var1: {var1}, var2: {var2}')

# Operador condicional ternário 

# menor = var1 if var1 < var2 else var2
# print(f'Menor valor: {menor}')

# Generators

# valores = [1,3,5,7,9,11,13,15]

# quadrados = (item**2 for item in valores)
# print(quadrados)
# for valores in quadrados:
#     print(valores)

# função enumerate()

# bebidas = ['cafe', 'cha', 'agua', 'suco', 'refrigerante']

# for i, item in enumerate(bebidas):
#     print(f'indice: {i}, Item: {item}')

temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0

for i, t in enumerate(temperaturas):
    if t < 0:
        print(f'A temperatura em {i} é negativa, com {t} graus C.')






