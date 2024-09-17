from contato import Contato

class Agenda:
    def __init__(self):
        self.__contatos = []  # Lista de contatos inicialmente vazia

    def inserir_contato(self, contato):
        self.__contatos.append(contato)  # Adiciona um contato à lista


    def buscar_contato(self, nome):
        for contato in self.__contatos:
            if contato.get_nome().lower() == nome.lower():
                return contato  # Retorna o contato se encontrado
        return None  # Retorna None se não encontrar o contato

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.__contatos.remove(contato)  # Remove o contato se encontrado
            return True
        return False  # Retorna False se o contato não for encontrado

    def listar_contatos(self):
        if not self.__contatos:
            print("Agenda vazia.")
        else:
            for contato in self.__contatos:
                contato.exibirContato()

