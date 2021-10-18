"""Construir o código necessário em Python para implementar o seguinte projeto:

O sistema possuirá uma classe abstrata chamada de Ferramenta que deve conteros atributos/propriedades nome, tensão e preço. 
Esta classe também deve possuir um método getInformacoes() que retorna todos os valores dos atributos. 
Esta classe também possui um método abstrato cadastrar().

O projeto também deve possuir as classes concretas, Furadeira e Lixadeira que herdam da classe Ferramenta.

A classe Furadeira deve possuir o atributo/propriedade fracamente privado potencia. Esta classe reimplementa o método getInformacoes() herdado de computador.

A classe Lixadeira possui o atributo/propriedade fortemente privado rotações. Esta classe reimplementa o método getInformacoes() herdado de computador.

Construa um menu com as opções para cadastrar as ferramentas suportadas pelo sistema.

Você pode enviar os arquivos do projeto ou criar um repositório no Github e enviar só o link do repositório.

"""

from abc import ABC, abstractclassmethod


class Ferramenta(ABC):

    @property
    def nome(self):
        pass

    @nome.setter
    @abstractclassmethod
    def nome(self, nome):
        pass

    @property
    def tensao(self):
        pass

    @tensao.setter
    @abstractclassmethod
    def tesao(self, tesao):
        pass

    @property
    def preco(self):
        pass

    @preco.setter
    @abstractclassmethod
    def preco(self, preco):
        pass

    
    def getInformacoes(self):
        print(f"""Modelo: {self.nome}
        Tensão: {self.tensao}
        Preço: {self.preco}""")


    @abstractclassmethod
    def cadastrar(self):
        pass
