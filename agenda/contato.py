from data import Data

class Contato:
    def __init__(self, nome, telefone, data_nascimento):
        self.__nome = nome
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento
    
    def get_nome(self):
        return self.__nome
    
    def get_telefone(self):
        return self.__telefone
    
    def get_data_nascimento(self):
        return self._da

    def exibirContato(self):
        print(f"Nome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
        print(self.__data_nascimento.getData())
    

        