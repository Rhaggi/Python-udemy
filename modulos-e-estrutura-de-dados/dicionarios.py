# chave, valor - arrays associativos

elemento = {
    'Z' : 3,
    'nome': 'litio',
    'grupo': 'metais alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionario tem {len(elemento)} elementos')

# atualizar uma entrada 

elemento['grupo'] = 'Alcalinos'

print(elemento)

#adicionar uma entrada

elemento['periodo'] = 1

print(elemento)

# exclusão de itens em dicionarios

# del elemento['periodo']

# print(elemento)

# elemento.clear()
# print(elemento)

# del elemento
# print(elemento)

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i,j in elemento.items():
    print(f'{i}: {j}')