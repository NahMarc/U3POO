from .Docente import Docente
from .Investigador import Investigador


class DocenteInvestigador(Docente, Investigador):
	__categoria: str
	__importeExtra: float

	def __init__(self, data: dict):
		super().__init__(data)
		self.__categoria = data['categoria']
		self.__importeExtra = data['importe']

	def getCategoria(self):
		return self.__categoria

	def getImporteExtra(self):
		return self.__importeExtra

	def calcularSueldo(self):
		return Docente.calcularSueldo(self) + self.__importeExtra

	def toJSON(self):
		return {
			**Docente.toJSON(self),
			**Investigador.toJSON(self),
			'categoria': self.__categoria,
			'importe': self.__importeExtra
		}
