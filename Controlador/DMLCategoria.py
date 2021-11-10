from Modelo.Categoria import Categoria
from DML import *


class DMLCategoria:

    @SQLABC(conexion=cnx)
    def alta(self, categoria: Categoria):
        return f"""INSERT INTO altas(id_categoria, nombre_categoria, descripcion_categoria) 
                   VALUES ({categoria.id},'{categoria.nombre}','{categoria.descripcion}')"""

    @SQLABC(conexion=cnx)
    def baja(self, id: int):
        return f"""DELETE FROM altas 
                   WHERE id_categoria={id}"""

    @SQLABC(conexion=cnx)
    def cambio(self, categoria: Categoria):
        return f"""UPDATE altas SET 
                   nombre_categoria='{categoria.nombre}', 
                   descripcion_categoria='{categoria.descripcion}' 
                   WHERE id_categoria={categoria.id}"""

    @SQLC(conexion=cnx)
    def consulta(self):
        return "SELECT * FROM altas"


if __name__ == '__main__':

    dml = DMLCategoria()

    categ = Categoria(1, "Hogar", "Articulos del hogar")
    dml.alta(categ)

    for cat in dml.consulta():
        print(cat)

    categ = Categoria(1, "Casa y jardin", "Articulos de casa y jardin")
    dml.cambio(categ)

    for cat in dml.consulta():
        print(cat)

    dml.baja(1)

    for cat in dml.consulta():
        print(cat)
