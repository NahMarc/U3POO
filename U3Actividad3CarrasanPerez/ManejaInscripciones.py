import numpy as np
from Inscripcion import Inscripcion
import csv


class ManejaInscripciones():

    def __init__(self, dimension = 1, incremento = 4):
        self.__arreglo = np.empty(dimension, dtype=Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregar_arre_inscrip(self, dato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = dato
        self.__cantidad += 1

    def MOSTRARINSC(self):
        for insc in self.__arreglo:
            print(insc)

    def validarpago(self,i):
        self.__arreglo[i].setpago()

    def guardarArchivo(self):
        data = {}
        lista = []
        for inscripto in self.__arreglo:
            if inscripto != None:
                taller = inscripto.gettaller()
                persona = inscripto.getPersona()
                fecha = inscripto.getfecha()
                pago = inscripto.getpago()
                data = {"dni": persona.getdni(), "IdTaller": taller.getid(),
                "FechaInscripcion": fecha, "Pago": pago}
                lista.append(data)
        print(lista)
        with open("inscripciones.csv", "w") as archivo:
            nombres = ["dni", "IdTaller", "FechaInscripcion", "Pago"]
            escribir = csv.DictWriter(archivo, fieldnames=nombres)
            escribir.writeheader()
            for datas in lista:
                escribir.writerow(datas)
