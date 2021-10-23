import datetime

from Modelo.Cliente import Cliente
from Modelo.ModoPago import ModoPago


class Factura:
    id: int
    cliente: Cliente
    pago: ModoPago
    fecha: datetime.datetime

    def __init__(self, id: int, cliente: Cliente, pago: ModoPago, fecha: datetime.datetime):
        self.id = id
        self.cliente = cliente
        self.pago = pago
        self.fecha = fecha
