import unittest
from Usado import Usado
from Nuevo import Nuevo
from Lista import ListaVehiculos


class TestListaVehiculos(unittest.TestCase):

    def testInsertarEnPosicion(self):
        lista = ListaVehiculos()
        vehiculo1 = Usado("Modelo1", 4, "Rojo", 10000, 'ABC 873', 249000, 1999)
        vehiculo2 = Nuevo("Modelo3", 4, "Verde", 200000, 'full')

        lista.insertarElemento(vehiculo1, 0) # Posición 0
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista.mostrarElemento(0), vehiculo1)

        lista.insertarElemento(vehiculo2, 2) # Ultima posición
        self.assertEqual(len(lista), 3)
        self.assertEqual(lista.mostrarElemento(2), vehiculo2)

        with self.assertRaises(ValueError): # Posición fuera de rango
            lista.insertarElemento(vehiculo2, 10)

    def testAgregarElemento(self):
        lista = ListaVehiculos()
        vehiculo1 = Usado("Modelo1", 4, "Rojo", 10000, 'oiu 333', 144655, 1999)
        vehiculo2 = Nuevo("Modelo2", 4, "Azul", 15000, 'full')

        lista.agregarElemento(vehiculo1)
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista.mostrarElemento(0), vehiculo1)

        lista.agregarElemento(vehiculo2)
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista.mostrarElemento(1), vehiculo2)

    def testObtenerObjetoEnPosicion(self):
        lista = ListaVehiculos()
        vehiculo1 = Usado("Modelo1", 4, "Rojo", 10000, 'ABC 873', 249000, 1999)
        vehiculo2 = Nuevo("Modelo3", 4, "Verde", 200000, 'full')

        lista.agregarElemento(vehiculo1)
        lista.agregarElemento(vehiculo2)

        self.assertEqual(lista.obtenerElementoEnPosicion(0), vehiculo1)
        self.assertEqual(lista.obtenerElementoEnPosicion(1), vehiculo2)

    def testModificarPrecioVenta(self):
        lista = ListaVehiculos()
        vehiculo1 = Usado("Modelo1", 4, "Rojo", 10000, 'ABC 873', 249000, 1999)

        lista.agregarElemento(vehiculo1)

        patente = vehiculo1.getPatente()
        precioFinal = lista.VentaPatente (patente)

        self.assertEqual(vehiculo1.getPrecioVenta(), precioFinal)

if '__name__' == '__main__':
    unittest.main()
