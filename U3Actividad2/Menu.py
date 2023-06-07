import os

class Menu:

    __switcher=None

    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            5: self.opc5,
                            0: self.salir
                        }

    def opcion(self,op, MS, MH):
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4 or op== 5:
            func(MS, MH)
        else:
            func()

    def mostrarMenu(self):
        print("""
----------Menu Principal----------

1: Registrar una venta de helado
2: Mostrar los 5 sabores de helado más vendidos
3: Estimar los gramos vendidos de un sabor determinado
4: Mostrar los sabores vendidos en una determinada cantidad
5: Informar el importe total recaudado en ventas
0: Salir
""")


    def opc1 (self, MS,  MH):
        os.system('cls')
        MH.venta(MS)


    def opc2 (self, MS,  MH):
        os.system('cls')
        mejoresVendidos = MS.mostrarMejores()
        print ('----------5 Sabores Mejor Vendidos----------')
        for sabor in mejoresVendidos:
            print(f"Sabor: {sabor.getNombreSabor()}, Cantidad vendida: {sabor.getContador()}")


    def opc3 (self, MS,  MH):
        os.system('cls')
        sabor = input ('Ingrese nombre del sabor de helado: ')
        r = MH.estimarGramos(sabor)
        print ('Se vendieron {:,.2f}gr del sabor {}'.format(r, sabor))


    def opc4 (self, MS, MH):
        os.system('cls')
        helado = float (input ('Ingrese la cantidad de helado: '))
        MH.saboresVendidos(helado)


    def opc5 (self, MS, MH):
        os.system('cls')
        print("----------Recaudación por tipo de helado----------")
        r = MH.recaudacionTotal()
        for gramos, precio in r.items():
            print (f'{gramos}g: ${precio}')


    def salir (self):
        print ('Hasta la proxima!!!')
