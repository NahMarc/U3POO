class Empleado():

    __dni=None
    __nombre=None
    __direccion=None
    __telefono=None

    def __init__ (self, dni, n, d, t):
        self.__dni = dni
        self.__nombre = n
        self.__direccion = d
        self.__telefono = t

    def getdni(self):
        return self.__dni

    def getnombre(self):
        return self.__nombre

    def getdireccion(self):
        return self.__direccion
