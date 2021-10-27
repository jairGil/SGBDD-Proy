from Modelo.Factura import Factura
from DML import *


class DMLFactura:
    @SQLABC(conexion=cnx)
    def alta(self, factura: Factura):
        return f"""INSERT INTO factura(id_factura, id_cliente, fecha_factura, id_modo_pago) 
                    VALUES ({factura.id},{factura.cliente.id}, 
                    TO_DATE('{factura.fecha.strftime("%m/%d/%Y %H:%M:%S")}', 'MM/DD/YYYY HH24:MI:SS'), 
                    {factura.pago.id})"""

    @SQLABC(conexion=cnx)
    def baja(self, id: int):
        return f"""DELETE FROM factura 
                       WHERE id_factura={id}"""

    @SQLABC(conexion=cnx)
    def cambio(self, factura: Factura):
        return f"""UPDATE factura SET 
                       id_cliente={factura.cliente.id}, 
                       fecha_factura=TO_DATE('{factura.fecha.strftime("%m/%d/%Y %H:%M:%S")}', 'MM/DD/YYYY HH24:MI:SS'), 
                       id_modo_pago={factura.pago.id}
                       WHERE id_factura={factura.id}"""

    @SQLC(conexion=cnx)
    def consulta(self):
        return "SELECT * FROM factura"


if __name__ == '__main__':
    from datetime import datetime
    from Modelo.ModoPago import ModoPago
    from Modelo.Cliente import Cliente
    from Controlador.DMLModoPago import DMLModoPago
    from Controlador.DMLCliente import DMLCliente

    dml_fact = DMLFactura()
    dml_mp = DMLModoPago()
    dml_clie = DMLCliente()

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
