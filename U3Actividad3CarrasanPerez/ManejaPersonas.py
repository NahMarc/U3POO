from Persona import Persona
from ManejaTalleres import ManejaTalleres


class ManejaPersonas():

    __Personas = []

    def __init__(self):
        self.__Personas = []

    def agregarP(self, persona):
        self.__Personas.append(persona)

    def mostrarpersona(self):
        for persona in self.__Personas:
            print(persona)

    def buscardni(self, ManejaTalleres, dni, id):
        i = 0
        while i < len(self.__Personas) and dni != int(self.__Personas[i].getdni()):
            i += 1

        if i < len(self.__Personas):
            print("Dni valido")
            ManejaTalleres.listar(id)

    def modifica(self, ManejaInscripciones, dni):
        i = 0
        while i < len(self.__Personas) and dni != int(self.__Personas[i].getdni()):
            i += 1
        if i < len(self.__Personas):
            ManejaInscripciones.validarpago(i)
