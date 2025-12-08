# indica a visibilidade de uma variavel no codigo

# escopo global e local

var_global = 'Curso completo de python'

def escreve_texto():
    global var_global
    var_global = 'Banco de dados com Fabio reis'
    var_local = 'Rosa Oliveira'
    print(f'Variável global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto')
    escreve_texto() 
    
    print(f'Tentar acessar as variaveis diretamente')
    print(f'Variável global: {var_global}')
    