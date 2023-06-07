class Sabor:

    __idSabor: int
    __ingrediente: str
    __nombreSabor: str
    __cont: int


    def __init__(self, idS, ing, nom) -> None:
        self.__idSabor = idS
        self.__ingrediente = ing
        self.__nombreSabor = nom
        self.__cont = 0


    def __str__(self) -> str:
        s = f'id del sabor: {self.getidSabor()}, ingredientes: {self.getIngredientes()}, nombre sabor: {self.getNombreSabor()}\n'
        return s


    def sumarContador (self):
        self.__cont += 1


    def getidSabor (self):
        return self.__idSabor


    def getIngredientes (self):
        return self.__ingrediente


    def getNombreSabor (self):
        return self.__nombreSabor


    def getContador(self):
        return self.__cont
