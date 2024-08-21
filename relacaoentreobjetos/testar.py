from capitulo import Capitulo
from livro import Livro
'''
numero = int(input("Digite o número do capítulo"))
titulo = input("Digite o título do capítulo")
texto = input("Digite o texto do capítulo")

capitulo1 = Capitulo(numero, titulo, texto)
capitulo1.exibirCapitulo()
'''

capitulo1 = Capitulo(1, "Introdução a Orientaçã a Objetos", "x.....")
capitulo2 = Capitulo(2, "Encapsulamento", "y.....")
capitulo3 = Capitulo(3, "Herança", "z.....")

livro_de_poo = Livro("Orientação a Objetos em Python", "Alba Lopes", 2024)
livro_de_poo.adicionarCapitulos(capitulo1)
livro_de_poo.adicionarCapitulos(capitulo2)
livro_de_poo.adicionarCapitulos(capitulo3)
livro_de_poo.imprimirLivro()
