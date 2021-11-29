from Modelo.Detalle import Detalle
from DML import *


class DMLDetalle:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def alta(self, detalle: Detalle):
        procedimiento = "sgbdd.alta_detalle"
        argumentos = [detalle.id, detalle.factura.id, detalle.producto.id, detalle.cantidad, detalle.precio]
        self.__dml.procedimiento(procedimiento, argumentos)

    def baja(self, id: int):
        self.__dml.bajas_cambios(f"""   
                                    DELETE FROM sgbdd.detalle 
                                    WHERE id_detalle={id}""")

    def cambio(self, detalle: Detalle):
        self.__dml.bajas_cambios(f"""
                        UPDATE sgbdd.detalle SET 
                        id_factura={detalle.id}, 
                        id_producto={detalle.producto.id}, 
                        cantidad_detalle={detalle.cantidad},
                        precio_detalle={detalle.precio}
                        WHERE id_detalle={detalle.id}""")

    def consulta(self):
        return self.__dml.consulta("SELECT * FROM sgbdd.detalle")


if __name__ == '__main__':
    from datetime import datetime
    from Modelo.ModoPago import ModoPago
    from Modelo.Cliente import Cliente
    from Modelo.Factura import Factura
    from Modelo.Producto import Producto
    from Modelo.Categoria import Categoria
    from Modelo.Marca import Marca
    from Controlador.DMLModoPago import DMLModoPago
    from Controlador.DMLCliente import DMLCliente
    from Controlador.DMLFactura import DMLFactura
    from Controlador.DMLProducto import DMLProducto
    from Controlador.DMLCategoria import DMLCategoria
    from Controlador.DMLMarca import DMLMarca

    cnx = Conexion("usr_administrador", "123", "localhost/xepdb1")

    dml_det = DMLDetalle(cnx)
    dml_fact = DMLFactura(cnx)
    dml_mp = DMLModoPago(cnx)
    dml_clie = DMLCliente(cnx)
    dml_prod = DMLProducto(cnx)
    dml_cat = DMLCategoria(cnx)
    dml_mar = DMLMarca(cnx)

    dml_det.baja(1)
    dml_fact.baja(1)
    dml_clie.baja(1)
    dml_mp.baja(1)
    dml_prod.baja(1)
    dml_cat.baja(1)
    dml_mar.baja(1)

    clie = Cliente(1, "algo@hot.com", "Juan", "Lopez", "1234567890")
    pago = ModoPago(1, "Efectivo", "Pagos en efectivo")
    fact = Factura(1, clie, pago, datetime.now())
    cat = Categoria(1, "Limpieza", "Articulos de limpieza")
    mar = Marca(1, "Fabuloso")
    prod = Producto(1, "Jabon", 35.5, 30, cat, mar)
    det = Detalle(1, fact, prod, 5, prod.precio)

    dml_mp.alta(pago)
    dml_clie.alta(clie)
    dml_fact.alta(fact)
    dml_cat.alta(cat)
    dml_mar.alta(mar)
    dml_prod.alta(prod)
    dml_det.alta(det)

    for det in dml_det.consulta():
        print(det)

    det = Detalle(1, fact, prod, 5, 1)

    dml_det.cambio(det)

    for det in dml_det.consulta():
        print(det)

    dml_det.baja(1)
    dml_fact.baja(1)
    dml_clie.baja(1)
    dml_mp.baja(1)
    dml_prod.baja(1)
    dml_cat.baja(1)
    dml_mar.baja(1)

    for det in dml_det.consulta():
        print(det)
