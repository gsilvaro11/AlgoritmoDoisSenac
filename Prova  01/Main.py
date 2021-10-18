
from types import NoneType
from Furadeira import Furadeira
from Lixadeira import Lixadeira



def menu():
    print(
    """
    0 - SAIR
    1 - CADASTRAR FURADEIRAS
    2 - CADASTRAR LIXADEIRA
    3 - LISTAR FURADEIRAS  
    4 - LISTAR LIXADEIRAS  
    """)

#Main
listaObjetoFuradeira = []
listaObjetoLixadeira = []
auxiliar = True
while auxiliar:
    menu()
    pergunta = int(input("Digite o indice: "))
    
    match pergunta:
        case 0:
            auxiliar = False
            
        case 1:
            nomeFuradeira = input("Digite o nome da furadiera: ")
            tensaoFuradeira = int(input("Tensão furadeira: "))
            precoFuradeira = float(input("Preço furadeira: "))
            potenciaFuradeira = float(input("Potencia furadeira: "))
            objetoFuradeira = Furadeira(nomeFuradeira, tensaoFuradeira, precoFuradeira, potenciaFuradeira)
            listaObjetoFuradeira.append([objetoFuradeira.nome, objetoFuradeira.tensao, objetoFuradeira.preco, objetoFuradeira.potencia])            
             
        case 2:            
            nomeLixadeira = input("Digite o nome da lixadeira: ")
            tensaoLixadeira = int(input("Tensão lixadeira: "))
            precoLixadeira = float(input("Preço lixadeira: "))
            rotacacaoLixadeira = float(input("Rotação lixadeira: "))
            objetoLixadeira = Lixadeira(nomeLixadeira, tensaoLixadeira, precoLixadeira, rotacacaoLixadeira)
            listaObjetoLixadeira.append([objetoLixadeira.nome, objetoLixadeira.tensao, objetoLixadeira.preco, objetoLixadeira.rotacao])

        case 3:            
            print(listaObjetoFuradeira)
             
        case 4:            
            print(listaObjetoLixadeira)

       
        case unknown_command:
            print("Erro, tente novamente")
        
