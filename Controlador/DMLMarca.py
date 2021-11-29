from Modelo.Marca import Marca
from DML import *


class DMLMarca:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def alta(self, marca: Marca):
        procedimiento = "sgbdd.alta_marca"
        argumentos = [marca.id, marca.nombre]
        self.__dml.procedimiento(procedimiento, argumentos)

    def baja(self, id: int):
        self.__dml.bajas_cambios(f"""
                                    DELETE FROM sgbdd.marca 
                                    WHERE id_marca={id}""")

    def cambio(self, marca: Marca):
        self.__dml.bajas_cambios(f"""
                                    UPDATE sgbdd.marca SET  
                                    nombre_marca='{marca.nombre}'  
                                    WHERE id_marca={marca.id}""")

    def consulta(self):
        return self.__dml.consulta("SELECT * FROM sgbdd.marca")


if __name__ == '__main__':
    cnx = Conexion("usr_administrador", "123", "localhost/xepdb1")

    dml = DMLMarca(cnx)

    mp = Marca(2, "Fabuloso")
    dml.alta(mp)

    for cat in dml.consulta():
        print(cat)

    mp = Marca(2, "Mr. Músculo")
    dml.cambio(mp)

    for cat in dml.consulta():
        print(cat)

    dml.baja(2)

    for cat in dml.consulta():
        print(cat)
