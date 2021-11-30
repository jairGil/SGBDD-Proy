import cx_Oracle

from Controlador.Conexion import Conexion
from Modelo.Producto import Producto
from Controlador.DML import DML


class DMLProducto:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def alta(self, producto: Producto):
        procedimiento = "sgbdd.alta_producto"
        argumentos = [producto.id, producto.nombre, producto.precio, producto.stock, producto.categoria.id,
                      producto.marca.id]
        self.__dml.procedimiento(procedimiento, argumentos)

    def baja(self, id: int):
        self.__dml.bajas_cambios(f"""
                                    DELETE FROM sgbdd.producto 
                                    WHERE id_producto={id}""")

    def cambio(self, producto: Producto):
        self.__dml.bajas_cambios(f"""
                                    UPDATE sgbdd.producto SET 
                                    prod = sgbdd.PRODUCTO_OBJ('{producto.nombre}', {producto.precio}), 
                                    stock={producto.stock}, 
                                    id_categoria={producto.categoria.id}, 
                                    id_marca={producto.marca.id} 
                                    WHERE id_producto={producto.id}""")

    def consulta(self):
        return self.__dml.consulta("SELECT * FROM sgbdd.producto")


if __name__ == '__main__':
    from Modelo.Marca import Marca
    from Modelo.Categoria import Categoria
    from Controlador.DMLCategoria import DMLCategoria
    from Controlador.DMLMarca import DMLMarca

    cnx = Conexion("usr_administrador", "123", "localhost/xepdb1")

    dml_prod = DMLProducto(cnx)
    dml_cat = DMLCategoria(cnx)
    dml_mar = DMLMarca(cnx)

    dml_prod.baja(1)
    dml_mar.baja(1)
    dml_cat.baja(1)

    m = Marca(1, "Fabuloso")
    c = Categoria(1, "Casa y jardin", "Articulos del hogar")
    p = Producto(1, "Jabon", 35.5, 30, c, m)

    dml_mar.alta(m)
    dml_cat.alta(c)
    dml_prod.alta(p)

    for cat in dml_prod.consulta():
        print(cat)

    p = Producto(1, "Jabon para trastes", 35.7605, 10, c, m)
    dml_prod.cambio(p)

    for cat in dml_prod.consulta():
        print(cat)

    dml_prod.baja(1)
    dml_mar.baja(1)
    dml_cat.baja(1)

    for cat in dml_prod.consulta():
        print(cat)
