from Modelo.Categoria import Categoria
from Controlador.DML import DML
from Controlador.Conexion import Conexion


class DMLCategoria:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def alta(self, categoria: Categoria):
        procedimiento = "sgbdd.alta_categoria"
        argumentos = [categoria.id, str(categoria.nombre), str(categoria.descripcion)]
        self.__dml.procedimiento(procedimiento, argumentos)

    def baja(self, id: int):
        self.__dml.bajas_cambios(f"""
                                    DELETE FROM sgbdd.categoria 
                                    WHERE id_categoria={id}""")

    def cambio(self, categoria: Categoria):
        self.__dml.bajas_cambios(f"""
            UPDATE sgbdd.categoria SET 
            nombre_categoria='{categoria.nombre}', 
            descripcion_categoria='{categoria.descripcion}' 
            WHERE id_categoria={categoria.id}""")

    def consulta(self):
        datos = self.__dml.consulta("""SELECT id_categoria, nombre_categoria, descripcion_categoria 
                                        FROM sgbdd.categoria""")
        return datos

    def consulta_tabla(self):
        encabezados = ["ID", "Nombre", "Descripcion", "Cantidad de productos"]
        datos = self.__dml.consulta("""
                                SELECT c.id_categoria, c.nombre_categoria, c.descripcion_categoria, count(p.id_producto)
                                FROM sgbdd.producto p 
                                JOIN categoria c ON c.id_categoria = p.id_categoria
                                GROUP BY c.id_categoria, c.nombre_categoria, c.descripcion_categoria 
                                ORDER BY c.id_categoria""")
        return encabezados, datos

    def obten_id(self):
        id = self.__dml.consulta("SELECT sgbdd.seq_categoria.nextval FROM dual")
        return id[0][0]


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
