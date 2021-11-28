from Modelo.Categoria import Categoria
from DML import *


class DMLCategoria:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def alta(self, categoria: Categoria):
        self.__dml.altas_bajas_cambios(f"""
            INSERT INTO sgbdd.categoria(id_categoria, nombre_categoria, descripcion_categoria) 
            VALUES ({categoria.id},'{categoria.nombre}','{categoria.descripcion}')""")

    def baja(self, id: int):
        self.__dml.altas_bajas_cambios(f"""
            DELETE FROM sgbdd.categoria 
            WHERE id_categoria={id}""")

    def cambio(self, categoria: Categoria):
        self.__dml.altas_bajas_cambios(f"""
            UPDATE sgbdd.categoria SET 
            nombre_categoria='{categoria.nombre}', 
            descripcion_categoria='{categoria.descripcion}' 
            WHERE id_categoria={categoria.id}""")

    def consulta(self):
        return self.__dml.consulta("SELECT * FROM sgbdd.categoria")


if __name__ == '__main__':
    cnx = Conexion("usr_administrador", "123", "localhost/xepdb1")

    dml = DMLCategoria(cnx)

    dml.baja(2)

    categ = Categoria(2, "Hogar", "Articulos del hogar")
    dml.alta(categ)

    for cat in dml.consulta():
        print(cat)

    categ = Categoria(2, "Casa y jardin", "Articulos de casa y jardin")
    dml.cambio(categ)

    for cat in dml.consulta():
        print(cat)

    dml.baja(2)

    for cat in dml.consulta():
        print(cat)
