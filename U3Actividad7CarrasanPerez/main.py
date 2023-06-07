from Menu import Menu
from src.GestorPersonal import GestorPesonal
from os import path

if __name__ == "__main__":
	gestor = GestorPesonal(path.dirname(__file__) + "/personal.json")
	menu = Menu(gestor)
	menu.iniciar()
