from Modelo.Producto import Producto
from DML import *


class DMLProducto:

    @SQLABC(conexion=cnx)
    def alta(self, producto: Producto):
        return f"""INSERT INTO producto(id_producto, nombre_producto, precio_producto, stock, id_categoria, id_marca) 
                   VALUES ({producto.id},'{producto.nombre}', {producto.precio}, {producto.stock}, 
                            {producto.categoria.id}, {producto.marca.id})"""

    @SQLABC(conexion=cnx)
    def baja(self, id: int):
        return f"""DELETE FROM producto 
                   WHERE id_producto={id}"""

    @SQLABC(conexion=cnx)
    def cambio(self, producto: Producto):
        return f"""UPDATE producto SET 
                   nombre_producto='{producto.nombre}', 
                   precio_producto={producto.precio}, 
                   stocK={producto.stock}, 
                   id_categoria={producto.categoria.id}, 
                   id_marca={producto.marca.id} 
                   WHERE id_producto={producto.id}"""

    @SQLC(conexion=cnx)
    def consulta(self):
        return "SELECT * FROM producto"


if __name__ == '__main__':
    from Modelo.Marca import Marca
    from Modelo.Categoria import Categoria
    from Controlador.DMLCategoria import DMLCategoria
    from Controlador.DMLMarca import DMLMarca

    dml_prod = DMLProducto()
    dml_cat = DMLCategoria()
    dml_mar = DMLMarca()

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
