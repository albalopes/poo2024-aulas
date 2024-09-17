from data import Data
from contato import Contato
from agenda import Agenda

def criar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    dia = int(input("Digite o dia de nascimento do contato: "))
    mes = int(input("Digite o mês de nascimento do contato: "))
    ano = int(input("Digite o ano de nascimento do contato: "))

    data_nasc = Data(dia, mes, ano)
    return Contato(nome, telefone, data_nasc)

def exibir_menu():
    print("\nMenu:")
    print("1. Inserir contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Listar todos os contatos")
    print("5. Sair")

agenda = Agenda()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        contato = criar_contato()
        agenda.inserir_contato(contato)
        print("Contato inserido com sucesso!")

    elif opcao == '2':
        nome = input("Digite o nome do contato que deseja buscar: ")
        contato = agenda.buscar_contato(nome)
        if contato:
            contato.exibirContato()
        else:
            print("Contato não encontrado.")

    elif opcao == '3':
        nome = input("Digite o nome do contato que deseja remover: ")
        if agenda.remover_contato(nome):
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == '4':
        agenda.listar_contatos()

    elif opcao == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
