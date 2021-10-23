from Modelo.Factura import Factura
from Modelo.Producto import Producto


class Detalle:
    id: int
    factura: Factura
    producto: Producto
    cantidad: int
    precio: float

    def __init__(self, id: int, factura: Factura, producto: Producto, cantidad: int, precio: float):
        self.id = id
        self.factura = factura
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
