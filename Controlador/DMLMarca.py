from Modelo.Marca import Marca
from DML import *


class DMLMarca:

    @SQLABC(conexion=cnx)
    def alta(self, marca: Marca):
        return f"""INSERT INTO marca(id_marca, nombre_marca)  
                   VALUES ({marca.id},'{marca.nombre}')"""

    @SQLABC(conexion=cnx)
    def baja(self, id: int):
        return f"""DELETE FROM marca 
                   WHERE id_marca={id}"""

    @SQLABC(conexion=cnx)
    def cambio(self, marca: Marca):
        return f"""UPDATE marca SET  
                   nombre_marca='{marca.nombre}'  
                   WHERE id_marca={marca.id}"""

    @SQLC(conexion=cnx)
    def consulta(self):
        return "SELECT * FROM marca"


if __name__ == '__main__':

    dml = DMLMarca()

    mp = Marca(1, "Fabuloso")
    dml.alta(mp)

    for cat in dml.consulta():
        print(cat)

    mp = Marca(1, "Mr. Músculo")
    dml.cambio(mp)

    for cat in dml.consulta():
        print(cat)

    dml.baja(1)

    for cat in dml.consulta():
        print(cat)
