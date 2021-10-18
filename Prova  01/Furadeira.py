"""
A classe Furadeira deve possuir o atributo/propriedade fracamente privado potencia. 
Esta classe reimplementa o método getInformacoes() herdado de computador.

"""

from Ferramenta import Ferramenta


class Furadeira(Ferramenta):
    def __init__(self, nome, tensao, preco, potencia) -> None:
        self._nome = nome
        self._tensao = tensao
        self._preco = preco
        self._potencia = potencia


    @property
    def nome(self):
        return self._nome

    @nome.setter    
    def nome(self, nome):
        self._nome = nome        

    @property
    def tensao(self):
        return self._tensao
        

    @tensao.setter    
    def tesao(self, tensao):
        self._tensao = tensao

    @property
    def preco(self):
        return self._preco        

    @preco.setter    
    def preco(self, preco):
        self._preco = preco

    
    @property
    def potencia(self):
        return self._potencia
    
    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

        
    def cadastrar(self):
        super().getInformacoes()
        print("Potencia: " + self._potencia)
