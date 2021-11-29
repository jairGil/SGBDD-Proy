from Controlador.Conexion import Conexion


class DML:
    conexion: Conexion

    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = None

    def bajas_cambios(self, sql):
        self.conexion.conectar()
        self.cursor = self.conexion.conexion.cursor()
        self.cursor.execute(sql)
        self.conexion.conexion.commit()
        self.conexion.desconectar()

    def consulta(self, sql):
        self.conexion.conectar()
        self.cursor = self.conexion.conexion.cursor()
        self.cursor.execute(sql)
        datos = self.cursor.fetchall()
        self.conexion.desconectar()
        return datos

    def procedimiento(self, proc: str, args: []):
        self.conexion.conectar()
        self.cursor = self.conexion.conexion.cursor()
        self.cursor.callproc(proc, args)
        self.conexion.conexion.commit()
        self.conexion.desconectar()
