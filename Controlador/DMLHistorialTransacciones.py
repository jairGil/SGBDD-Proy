from Controlador.Conexion import Conexion
from Controlador.DML import DML


class DMLHistorialTransacciones:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def consulta(self):
        encabezados = ["ID Transaccion", "Tabla", "Transaccion", "Usuario", "Fecha"]
        datos = self.__dml.consulta("""SELECT id_transaccion, tabla, tipo_transaccion, usuario, fecha_transaccion
                                        FROM sgbdd.transacciones 
                                        ORDER BY fecha_transaccion""")
        return encabezados, datos
