from data import Data
from contato import Contato

nome = input("Digite o nome do contato: ")
telefone = input("Digite o telefone do contato: ")
dia = int(input("Digite o dia de nascimento do contato: "))
mes = int(input("Digite o mês de nascimento do contato: "))
ano = int(input("Digite o ano de nascimento do contato: "))

data_nasc = Data(dia, mes, ano)
contato = Contato(nome, telefone, data_nasc)
contato.exibirContato()