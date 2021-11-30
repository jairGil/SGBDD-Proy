from Controlador.Conexion import Conexion
from Controlador.DML import DML


class DMLHistorialProducto:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def consulta(self):
        encabezados = ["ID Prodcuto", "Fecha", "Nombre anterior", "Precio anterior", "Nombre nuevo", "Precio nuevo"]
        datos = self.__dml.consulta("""SELECT   p.id_producto, p.fecha_modificacion, 
                                                p.prod_anterior.nombre nombre, p.prod_anterior.precio precio,
                                                p.prod_nuevo.nombre nombre1, p.prod_nuevo.precio precio1
                                        FROM sgbdd.historial_producto p""")
        return encabezados, datos
