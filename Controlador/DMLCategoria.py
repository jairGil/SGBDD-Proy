from Modelo.Categoria import Categoria
from DML import *


class DMLCategoria:
    conexion = Conexion("SGBDD", "123", "localhost/xepdb1")

    @SQLABC(conexion=conexion)
    def alta(self, categoria: Categoria):
        return f"INSERT INTO categoria(id_categoria, nombre_categoria, descripcion_categoria) " \
               f"VALUES ({categoria.id},'{categoria.nombre}','{categoria.descripcion}')"

    @SQLABC(conexion=conexion)
    def baja(self, id: int):
        return f"DELETE FROM categoria " \
               f"WHERE id_categoria={id}"

    @SQLABC(conexion=conexion)
    def cambio(self, categoria: Categoria):
        return f"UPDATE categoria SET " \
               f"nombre_categoria='{categoria.nombre}'," \
               f"descripcion_categoria='{categoria.descripcion}'" \
               f"WHERE id_categoria={categoria.id}"

    @SQLC(conexion=conexion)
    def consulta(self):
        return "SELECT * FROM categoria"


if __name__ == '__main__':

    dml = DMLCategoria()

    categ = Categoria(1, "Pago", "pago")
    dml.alta(categ)

    for cat in dml.consulta():
        print(cat)

    categ = Categoria(1, "Efectivo", "Pagos en efectivo")
    dml.cambio(categ)

    for cat in dml.consulta():
        print(cat)

    dml.baja(1)

    for cat in dml.consulta():
        print(cat)
