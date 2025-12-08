tupla = (2,4,6,7,9)

print(tupla)

halogenios = ('F', 'cl', 'br', 'i', 'at')

gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')

elementos = halogenios + gases_nobres

t1 = (5,2,6,8,4,5,6,4,0,12,33,3,4,5)

print('cl' in halogenios)

# Operações que não podem ser feitos com a tupla: .sort(), .append(), .reverse(), .pop() - ou seja, aquilo que altere a tupla

# for elemento in elementos:
#     print(f'Elemento quimico: {elemento}')

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)

print(sorted(alcalinos))