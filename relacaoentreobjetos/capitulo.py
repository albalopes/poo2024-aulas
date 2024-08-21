class Capitulo:
    def __init__(self, numero, titulo, texto):
        self.__numero = numero
        self.__titulo = titulo
        self.__texto = texto
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
    
    def setNumero(self, numero):
        self.__numero = numero
    
    def setTexto(self, texto):
        self.__texto = texto

    def getTitulo(self):
        return self.__titulo
    
    def getNumero(self):
        return self.__numero
    
    def getTexto(self):
        return self.__texto