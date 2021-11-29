import cx_Oracle

from Modelo.Factura import Factura
from DML import *


class DMLFactura:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def alta(self, factura: Factura):
        procedimiento = "sgbdd.alta_factura"
        argumentos = [factura.id, factura.cliente.id, factura.pago.id]
        self.__dml.procedimiento(procedimiento, argumentos)

    def baja(self, id: int):
        self.__dml.bajas_cambios(f"""
                                    DELETE FROM sgbdd.factura 
                                    WHERE id_factura={id}""")

    def cambio(self, factura: Factura):
        self.__dml.bajas_cambios(f"""
                                    UPDATE sgbdd.factura SET 
                                    id_cliente={factura.cliente.id}, 
                                    fecha_factura=TO_DATE('{factura.fecha.strftime("%m/%d/%Y %H:%M:%S")}', 
                                                            'MM/DD/YYYY HH24:MI:SS'), 
                                    id_modo_pago={factura.pago.id}
                                    WHERE id_factura={factura.id}""")

    def consulta(self):
        return self.__dml.consulta("SELECT * FROM sgbdd.factura")


if __name__ == '__main__':
    from datetime import datetime
    from Modelo.ModoPago import ModoPago
    from Modelo.Cliente import Cliente
    from Controlador.DMLModoPago import DMLModoPago
    from Controlador.DMLCliente import DMLCliente

    cnx = Conexion("usr_administrador", "123", "localhost/xepdb1")

    dml_fact = DMLFactura(cnx)
    dml_mp = DMLModoPago(cnx)
    dml_clie = DMLCliente(cnx)

    dml_fact.baja(1)
    dml_clie.baja(1)
    dml_mp.baja(1)

    clie = Cliente(1, "algo@hot.com", "Juan", "Lopez", "1234567890")
    pago = ModoPago(1, "Efectivo", "Pagos en efectivo")
    fact = Factura(1, clie, pago, datetime.now())

    dml_mp.alta(pago)
    dml_clie.alta(clie)
    dml_fact.alta(fact)

    for cat in dml_fact.consulta():
        print(cat)

    clie = Cliente(1, "algo@hot.com", "Juan", "Lopez", "1234567890")
    pago = ModoPago(1, "Efectivo", "Pagos en efectivo")
    fact = Factura(1, clie, pago, datetime.today())

    dml_fact.cambio(fact)

    for cat in dml_fact.consulta():
        print(cat)

    dml_fact.baja(1)
    dml_mp.baja(1)
    dml_clie.baja(1)

    for cat in dml_fact.consulta():
        print(cat)
