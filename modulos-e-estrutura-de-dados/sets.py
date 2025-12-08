# armazena items não duplicados

# planeta_anao = {'plutao', 'ceres', 'eris', 'haumea', 'makemake'}

# print(planeta_anao)

# print('lua' not in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper())

astros1 = {'lua', 'venus', 'sirius', 'marte', 'lua'}
astros2 = {'lua', 'venus', 'sirius', 'marte', 'cometa de harley'}

print(astros1 | astros2)
print(astros1.union(astros2))

# astros_set = set(astros)

# print(astros_set)