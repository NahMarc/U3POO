class Helado:

    __gramos: float
    __precio: float
    __sabor = []

    def __init__(self, g, p, s = None) -> None:
        self.__gramos = g
        self.__precio = p
        if s != None:
            self.addSabor (s, 1)


    def addSabor (self, sabor, cant=1):
        for i in range (cant):
            self.__sabor.append(sabor)


    def getGramos (self):
        return float (self.__gramos)


    def getPrecio (self):
        return self.__precio


    def getSabores(self):
        return self.__sabor
