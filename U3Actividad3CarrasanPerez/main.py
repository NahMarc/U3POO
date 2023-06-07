"""
Clase asociación
Con su grupo de trabajo deben desarrollar una aplicación para manejar las inscripciones de las personas a los talleres
de capacitación que se dictan en una escuela complementaria. Al momento de la inscripción la persona puede o no abonar
el costo del taller.

 a-    Defina las clases involucradas en el siguiente diagrama.

 a-    Defina una clase con un atributo arreglo para almacenar instancias de la clase TallerCapacitacion. El archivo
“Talleres.csv” contiene en la primera línea la cantidad de talleres, y a continuación los datos de cada uno de ellos.
 b-    Defina una clase colección (manejador), tipo lista para almacenar las instancias de la clase Persona.
 c-     Defina una clase colección (manejador), tipo arreglo para almacenar instancias de la clase Inscripcion.
 d- Implementar un programa que permita:

 1.     Cargar los datos de los talleres en la clase TallerCapacitacion a partir de los datos registrados en el archivo.
 2.     Inscribir una persona en un taller: Se registra la inscripción (con el atributo pago en False) y la cantidad de
 vacantes del taller debe ser actualizada.
 3.     Consultar inscripción: Ingresar el DNI de una persona, si está inscripta mostrar el nombre del taller en el que
 se inscribió y el monto que adeuda.
 4.     Consultar inscriptos: Ingresar el identificador de un taller y listar los datos de los alumnos que se
 inscribieron en él.
 5.     Registrar pago: Ingresar el DNI de una persona y registrar el pago (dar al atributo pago el valor True).
 6.     Guardar inscripciones: Generar un nuevo archivo que contenga los siguientes datos de las inscripciones: DNI de
 la persona, idTaller, fechaInscripcion y pago.
 
"""

from ManejaTalleres import ManejaTalleres
from TallerCapacitacion import Taller
from Persona import Persona
from ManejaPersonas import ManejaPersonas
from ManejaInscripciones import ManejaInscripciones
import csv


if __name__ == "__main__":
    archivo = open("Talleres.csv")
    leer = csv.reader(archivo, delimiter=";")
    bandera = 0
    ban = 0
    for taller in leer:
        if len(taller) != 0:
            if bandera == 0:
                bandera = 1
            else:
                if ban == 0:
                    ManejaTalleres = ManejaTalleres(int(taller[0]))
                    ban = 1
                else:
                    talleres = Taller(int(taller[0]), taller[1], int(taller[2]), int(taller[3]))
                    ManejaTalleres.AgregarTaller(talleres)
        else:
            print("Hay un error en el archivo CSV")
    archivo.close()
    ManejaPersonas = ManejaPersonas()
    ManejaInscripciones = ManejaInscripciones()
    print("Realizar una incripcion")
    Nombre = (input("Ingrese nombre: "))
    direccion = (input("Ingrese direccion: "))
    dni = input("Ingrese dni: ")
    persona = Persona(Nombre, direccion, dni)
    ManejaPersonas.agregarP(persona)
    print("Ingreso de fecha")
    anio = input("Ingrese año: ")
    mes = input("Ingrese mes: ")
    dia = input("Ingrese dia: ")
    fecha_inscripcion = str(dia)+"/"+str(mes)+"/"+str(anio)
    print("Seleccione taller a inscribir")
    ManejaTalleres.Mostrar()
    id = int(input(""))
    i = ManejaTalleres.buscar(id)
    while i == -1:
        print("Eleccion no valida, vuelva a seleccionar taller")
        id = int(input(""))
        i = ManejaTalleres.buscar(id)
    print("Dato valido")
    objeto = ManejaTalleres.registrar(fecha_inscripcion, persona, i)
    ManejaInscripciones.agregar_arre_inscrip(objeto)

    print("Mostrar Innscripciones")
    ManejaInscripciones.MOSTRARINSC()
    print("******item 3******")
    dni = int(input("Ingrese dni para mostrar Taller + monto adeudado: "))
    ManejaPersonas.buscardni(ManejaTalleres, dni, id)
    print("******item 4******")
    id = int(input("Ingrese id a listar:"))
    ManejaTalleres.item4(id, ManejaPersonas)
    print("******item 5******")
    dni = int(input("Ingrese dni a pagar monto adeudado: "))
    ManejaPersonas.modifica(ManejaInscripciones, dni)
    print("******item 6******")
    ManejaInscripciones.guardarArchivo()
    print("Programa finalizado, hasta luego!!!")
