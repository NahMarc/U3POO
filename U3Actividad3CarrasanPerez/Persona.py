class Persona():

    __nombre = ""
    __direccion = ""
    __dni = 0

    def __init__(self, nom, dir, dni):
        self.__nombre = nom
        self.__direccion = dir
        self.__dni = dni

    def __str__(self):
        s ="\nnombre :{}".format(self.__nombre)
        s += "\ndireccion :{}".format(self.__direccion)
        s += "\ndni :{}".format(self.__dni)
        s += "\n"
        return s

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getDni(self):
        return self.__dni
