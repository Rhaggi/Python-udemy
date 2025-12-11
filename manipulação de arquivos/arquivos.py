# Manipulação de arquivos de texto

# Ler o arquivo

manipulador = open(r'C:\Users\RosalinaTeixeiraOliv\Documents\Cursos\Python udemy\manipulação de arquivos\arquivo.txt', 'r', encoding='utf-8')

# print(f'Usando o método read(): \n')

# #print(manipulador.read())

# print(manipulador.readlines())

# texto = input('Qual texto deseja procurar no arquivo?:')

try:
    manipulador = open(r'C:\Users\RosalinaTeixeiraOliv\Documents\Cursos\Python udemy\manipulação de arquivos\arquivo.txt', 'r', encoding='utf-8')
#     for linha in manipulador:
#         if texto in linha: 
#             print(f'A string foi encontrada!')
#             print(linha)
#         else: 
#             print('String não encontrada')
except IOError:
    print('Não foi possivel abrir o arquivo')
else: 
    manipulador.close()

# Escrever em arquivos

