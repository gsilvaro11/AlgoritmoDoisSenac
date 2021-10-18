"""A classe Lixadeira possui o atributo/propriedade fortemente privado rotações.
Esta classe reimplementa o método getInformacoes() herdado de Ferramenta.
"""

from Ferramenta import Ferramenta


class Lixadeira(Ferramenta):
    def __init__(self, nome, tensao, preco, rotacao) -> None:
        self._nome = nome
        self._tensao = tensao
        self._preco = preco
        self.__rotacao = rotacao
    
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
    def rotacao(self):
        return self.__rotacao
    
    @rotacao.setter
    def rotacao(self, rotacao):
        self.__rotacao = rotacao

    def cadastrar(self):
        super().getInformacoes()
        print("Rotações: " + self.__rotacao)