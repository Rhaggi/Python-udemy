# Orientação a objetos - Paradigma de programação
# classes e objetos

class Veiculo: 
    def movimentar(self):
        print(f'Sou um veiculo e me desloco')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Setter - Permite gravar dados em elementos

    def set_num_registro(self, registro):
        self.__num_registro = registro


    # Getter - permite acessar os elementos e atributos dentro da classe

    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}')

    def get_num_registro(self):
        return self.__num_registro
    

class Carro(Veiculo):
    # Metodo __init__ será herdado

    def movimentar(self):
        print(f'Sou um carro andando pelas ruas')


if __name__ == '__main__':

    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()

    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro(12345)

    print(f'Registro: {meu_veiculo.get_num_registro()}\n')

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()
