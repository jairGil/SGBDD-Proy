from Modelo.Detalle import Detalle
from DML import *


class DMLDetalle:
    @SQLABC(conexion=cnx)
    def alta(self, detalle: Detalle):
        return f"""INSERT INTO detalle (id_detalle, id_factura, id_producto, cantidad_detalle, precio_detalle) 
                    VALUES ({detalle.id}, {detalle.factura.id}, {detalle.producto.id}, {detalle.cantidad}, 
                    {detalle.precio})"""

    @SQLABC(conexion=cnx)
    def baja(self, id: int):
        return f"""DELETE FROM detalle 
                       WHERE id_detalle={id}"""

    @SQLABC(conexion=cnx)
    def cambio(self, detalle: Detalle):
        return f"""UPDATE detalle SET 
                       id_factura={detalle.id}, 
                       id_producto={detalle.producto.id}, 
                       cantidad_detalle={detalle.cantidad},
                       precio_detalle={detalle.precio}
                       WHERE id_detalle={detalle.id}"""

    @SQLC(conexion=cnx)
    def consulta(self):
        return "SELECT * FROM detalle"


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

    dml_det = DMLDetalle()
    dml_fact = DMLFactura()
    dml_mp = DMLModoPago()
    dml_clie = DMLCliente()
    dml_prod = DMLProducto()
    dml_cat = DMLCategoria()
    dml_mar = DMLMarca()

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
