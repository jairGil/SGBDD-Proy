from cx_Oracle import Cursor
from Conexion import Conexion

cnx = Conexion("SGBDD", "123", "localhost/xepdb1")


class SQLABC:
    conexion: Conexion
    cursor: Cursor

    def __init__(self, conexion):
        self.conexion = conexion

    def __call__(self, original_func):
        decorator_self = self

        def c(*args):
            decorator_self.conexion.conectar()
            decorator_self.cursor = decorator_self.conexion.conexion.cursor()

            sql = original_func(*args)

            decorator_self.cursor.execute(sql)
            decorator_self.conexion.conexion.commit()
            decorator_self.conexion.desconectar()
        return c


class SQLC:
    con: Conexion
    cursor: Cursor

    def __init__(self, conexion):
        self.con = conexion

    def __call__(self, original_func):
        decorator_self = self

        def c(*args):
            decorator_self.con.conectar()
            decorator_self.cursor = decorator_self.con.conexion.cursor()

            sql = original_func(*args)

            datos = list(decorator_self.cursor.execute(sql))
            decorator_self.con.desconectar()
            return datos
        return c


if __name__ == '__main__':

    @SQLC(conexion=con)
    def select():
        return "select * from employees where employee_id=200"


    @SQLC(conexion=con)
    def select_id(id: int):
        return f"select * from employees where employee_id={id}"

    for element in select():
        print(element)

    print(select_id(130))
