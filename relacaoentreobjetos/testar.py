from capitulo import Capitulo

numero = int(input("Digite o número do capítulo"))
titulo = input("Digite o título do capítulo")
texto = input("Digite o texto do capítulo")

capitulo1 = Capitulo(numero, titulo, texto)
capitulo1.exibirCapitulo()