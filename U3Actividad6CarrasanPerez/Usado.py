from Vehiculo import Vehiculo


class Usado(Vehiculo):
    __patente: str
    __km: int
    __anio: int

    def __init__(self, mod, cantPuertas, color, precioBase, patente, km, anio) -> None:
        super().__init__(mod, cantPuertas, color, precioBase)
        self.__patente = patente
        self.__km = km
        self.__anio = año

    def __str__(self) -> str:
        s = f'Modelo: {super().getModelo()}, Cant. de puertas: {super().getCantidadPuertas()}, Color: {super().getColor()}, precio base: {super().getPrecioBase()}, patente: {self.__patente}, kilometros: {self.__km}, año: {self.__anio}'
        return s

    def __str__(self) -> str:
        return super().__str__()

    def getPatente(self):
        return self.__patente

    def getKm(self):
        return self.__km

    def getAnio(self):
        return self.__anio

    def setPrecioBase(self, precio):
        super().setPB(precio)
