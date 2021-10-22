import cx_Oracle


class Conexion:
    usuario: str
    contrasena: str
    dsn: str
    conexion: cx_Oracle

    def __init__(self, usuario, contrasena, dsn):
        self.usuario = usuario
        self.contrasena = contrasena
        self.dsn = dsn

    def conectar(self):
        try:
            self.conexion = cx_Oracle.connect(user=self.usuario, password=self.contrasena, dsn=self.dsn)
        except ConnectionError:
            print("ERROR")

    def desconectar(self):
        self.conexion.close()


if __name__ == '__main__':
    con = Conexion("SGBDD", "123", "localhost/xepdb1")
    con.conectar()

    cur = con.conexion.cursor()
    rows = list(cur.execute("select * from modo_pago"))

    for i in rows:
        print(i)

    print(len(rows))

    for column in cur.description:
        print(column)

    con.desconectar()
