from zope.interface import Interface, implementer

class IColeccion(Interface):  # type: ignore
	def insertarElemento(self, posicion, elemento):
		pass
	def agregarElemento(self, elemento):
		pass
	def mostrarElemento(self, posicion):
		pass
