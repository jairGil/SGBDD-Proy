from Modelo.ModoPago import ModoPago
from DML import *


class DMLModoPago:

    @SQLABC(conexion=cnx)
    def alta(self, modo_pago: ModoPago):
        return f"""INSERT INTO modo_pago(id_modo_pago, nombre_modo_pago, detalles_modo_pago) 
                   VALUES ({modo_pago.id},'{modo_pago.nombre}','{modo_pago.detalles}')"""

    @SQLABC(conexion=cnx)
    def baja(self, id: int):
        return f"""DELETE FROM modo_pago 
                   WHERE id_modo_pago={id}"""

    @SQLABC(conexion=cnx)
    def cambio(self, modo_pago: ModoPago):
        return f"""UPDATE modo_pago SET 
                   nombre_modo_pago='{modo_pago.nombre}', 
                   detalles_modo_pago='{modo_pago.detalles}' 
                   WHERE id_modo_pago={modo_pago.id}"""

    @SQLC(conexion=cnx)
    def consulta(self):
        return "SELECT * FROM modo_pago"


if __name__ == '__main__':

    dml = DMLModoPago()

    mp = ModoPago(1, "Efectivo", "Pagos en efectivo")
    dml.alta(mp)

    for cat in dml.consulta():
        print(cat)

    mp = ModoPago(1, "Tarjeta", "Pagos con tarjeta")
    dml.cambio(mp)

    for cat in dml.consulta():
        print(cat)

    dml.baja(1)

    for cat in dml.consulta():
        print(cat)
