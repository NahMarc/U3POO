class Taller():

    __idTaller = None
    __nombre = None
    __vacantes = None
    __montoInscripcion = None
    __listaInscriptos = None

    def __init__(self, id, nom, vac, monto):
        self.__idTaller = id
        self.__nombre = nom
        self.__vacantes = vac
        self.__montoInscripcion = monto
        self.__listaInscriptos = []

    def __str__ (self):
        return "   {}               {}             {}          {}".format(int(self.__idTaller), str(self.__nombre), int(self.__vacantes), self.__montoInscripcion)

    def agregar(self, algo):
        self.__listaInscriptos.append(algo)
        self.__vacantes -= 1

    def getid(self):
        return int(self.__idTaller)

    def getvacantes(self):
        return int(self.__vacantes)

    def getTaller(self):
        return self.__nombre

    def getMonto(self):
        return self.__montoInscripcion
    
    def acceder(self):
        for i in self.__listaInscriptos:
            print(i)
