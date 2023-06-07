import csv
from Sabor import Sabor


class manejadorSabores:

    __Sabores: list


    def __init__(self) -> None:
        self.__Sabores = []


    def __str__(self) -> str:
        s = ''
        for sabor in self.__Sabores:
            s += str(sabor)
        return s


    def addSabor (self, s):
        self.__Sabores.append(s)


    def carga (self):
        path = './sabores.csv'
        file = open (path, 'r')
        reader = csv.reader (file, delimiter=';')
        flag = True
        for row in reader:
            if flag:
                flag = False
            else:
                idSabor = row[0]
                ing = row[1]
                nomSab = row[2]
                xSabor = Sabor (idSabor, ing, nomSab)
                self.addSabor(xSabor)
                print ('carga lista')
        file.close()


    def sumarContador (self, i):
        self.__Sabores[i].sumarContador()


    def mostrarMejores(self):
        sabores_ordenados = sorted(self.__Sabores, key=lambda sabor: sabor.getContador(), reverse=True)
        return sabores_ordenados[:5]


    def getSaborPorId (self, i):
        return self.__Sabores[i]
