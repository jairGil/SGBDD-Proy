from Controlador.Conexion import Conexion
from Modelo.ModoPago import ModoPago
from Controlador.DML import DML


class DMLModoPago:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def alta(self, modo_pago: ModoPago):
        procedimiento = "sgbdd.alta_modo_pago"
        argumentos = [modo_pago.id, modo_pago.nombre, modo_pago.detalles]
        self.__dml.procedimiento(procedimiento, argumentos)

    def baja(self, id: int):
        self.__dml.bajas_cambios(f"""
                                    DELETE FROM sgbdd.modo_pago 
                                    WHERE id_modo_pago={id}""")

    def cambio(self, modo_pago: ModoPago):
        self.__dml.bajas_cambios(f"""
                                    UPDATE sgbdd.modo_pago SET 
                                    nombre_modo_pago='{modo_pago.nombre}', 
                                    detalles_modo_pago='{modo_pago.detalles}' 
                                    WHERE id_modo_pago={modo_pago.id}""")

    def consulta(self):
        encabezados = ["ID", "Nombre", "Detalles"]
        datos = self.__dml.consulta("SELECT * FROM sgbdd.modo_pago")
        return encabezados, datos

    def obten_id(self):
        id = self.__dml.consulta("SELECT sgbdd.seq_modo_pago.nextval FROM dual")
        return id[0][0]


if __name__ == '__main__':
    cnx = Conexion("usr_administrador", "123", "localhost/xepdb1")

    dml = DMLModoPago(cnx)

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
