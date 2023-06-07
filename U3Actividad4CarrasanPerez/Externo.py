from Empleado import Empleado


class Externo(Empleado):

    __tarea = None
    __fechaInicio = None
    __fechaFin = None
    __MontoViatico = None
    __costo = None
    __Montoseguro = None

    def __init__(self, dni, nom, dir, tel, fei, fef, ta, mv, costo, ms):
        super(). __init__(dni, nom, dir, tel)
        self.__fechaInicio = fei
        self.__fechaFin = fef
        self.__tarea = ta
        self.__MontoViatico = mv
        self.__costo = costo
        self.__Montoseguro = ms

    def gettarea(self):
        return self.__tarea

    def getcosto(self):
        return self.__costo

    def gethora(self):
        return self.__fechaFin

    def ext(self):
        sueldo = 0
        sueldo = float(self.__costo) - int(self.__MontoViatico) - float(self.__Montoseguro)
        return sueldo
