import os
from Menu import Menu
from ManejaSabores import manejadorSabores
from ManejaHelados import manejadorHelados


if __name__ == '__main__':
    MH = manejadorHelados()
    MS = manejadorSabores()
    MS.carga()
    bandera = False
    os.system('cls')
    menu = Menu()
    while not bandera:
        menu.mostrarMenu()
        opcion = int(input("Su opcion: "))
        menu.opcion(opcion, MS, MH)
        if opcion == 0:
            bandera = True
        os.system('cls')
    os.system('exit')
