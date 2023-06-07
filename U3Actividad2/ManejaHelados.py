from Helado import Helado


class manejadorHelados:

    __Helados: list

    def __init__(self) -> None:
        self.__Helados = []


    def addHelado(self, h):
        self.__Helados.append(h)


    def __str__(self) -> str:
        s = ''
        for helado in self.__Sabores:
            s += str(helado)
        return s


    def venta (self, MS):
        g = int (input ('Ingrese cantidad de gramos del helado (100, 150, 250, 500 y 1000): '))
        p = int (input ('Ingrese Precio: '))
        cant = int (input ('Ingrese numero de sabores: '))
        print ('Escoja un sabor:')
        print (str(MS))
        xHelado = Helado (g, p)
        self.addHelado(xHelado)
        j = 1
        for i in range (cant):
            xId = int (input (f'Ingrese id del sabor {j}: '))
            sabor = MS.getSaborPorId(xId-1)
            MS.sumarContador(xId-1)
            xHelado.addSabor(sabor)
            j += 1


    def mostrarPedido (self, xh):
        print(f'''
Pedido: 
gramos: {xh.getGramos()}
sabores:''')
        for sabor in xh.getSabores():
            print (str (sabor))
            print (sabor.getContador())


    def calculoGramos (self, g, cant):
        return g/cant


    def estimarGramos (self, xs):
        r = 0
        for h in self.__Helados:
            for s in h.getSabores():
                if xs == s.getNombreSabor():
                    g = h.getGramos()
                    r += float(self.calculoGramos(g, len(h.getSabores())))
        return r


    def saboresVendidos (self, xh):
        print (f'---------->sabores vendidos en {int(xh)}g <----------')
        aux = ''
        for h in self.__Helados:
            if h.getGramos() == xh:
                for s in h.getSabores():
                    if s != aux:
                        print (f'{s.getNombreSabor()}')
                        aux = s.getNombreSabor()


    def recaudacionTotal(self):
        r = {}
        for h in self.__Helados:
            precio = h.getPrecio()
            gramos = h.getGramos()
            if gramos not in r:
                r[gramos] = precio
            else: r[gramos] += precio
        return r

