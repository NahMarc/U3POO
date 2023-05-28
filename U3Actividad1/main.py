from os import path
from Menu import Menu
from ManejaFacultades import ManejadorFacultades


def opcion1(manejadorFacultades: ManejadorFacultades):
    codigoFacultad = input("Ingrese el código de la facultad: ")

    facultad = manejadorFacultades.obtenerFacultad(codigoFacultad)

    if facultad is None:
        print(f"No existe la facultad {codigoFacultad}")
    else:
        print(f"\nNombre de la facultad: {facultad.getNombre()}")
        print("Carreras de la facultad: \n")
        for key, value in facultad.getCarreras().items():
            print(f"\t{key}: {value.getNombre()}")
            print(f"\tDuración: {value.getDuracion()}\n")


def opcion2(manejadorFacultades: ManejadorFacultades):
    nombreCarrera = input("Ingrese el nombre de la carrera: ")

    resultado = manejadorFacultades.encontrarCarreraPorNombre(nombreCarrera)

    if resultado is None:
        print(f"No existe la carrera {nombreCarrera}")
    else:
        facultad, carrera = resultado
        print(f"\nCódigo {facultad.getCodigo()}:{carrera.getCodigo()}")
        print(f"Facultad donde se dicta: {facultad.getNombre()}")
        print(f"Localidad: {facultad.getLocalidad()}")


if __name__ == '__main__':
    manejador = ManejadorFacultades(path.dirname(__file__) + '/Facultades.csv')

    menu = Menu()
    menu.registrarOpcion('1', 'Mostrar facultad y carreras', opcion1, manejador)
    menu.registrarOpcion('2', 'Encontrar carrera por nombre', opcion2, manejador)
    menu.iniciar()
