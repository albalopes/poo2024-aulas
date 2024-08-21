from capitulo import Capitulo

class Livro:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__capitulos = []
    
    def adicionarCapitulos(self, capitulo):
        self.__capitulos.append(capitulo)

    def imprimirLivro(self):
        for cap in self.__capitulos:
            cap.exibirCapitulo() 
            