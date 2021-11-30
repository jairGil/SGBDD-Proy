from Controlador.Conexion import Conexion
from Modelo.Cliente import Cliente
from Controlador.DML import DML


class DMLCliente:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__dml = DML(self.__conexion)

    def alta(self, cliente: Cliente):
        procedimiento = "sgbdd.alta_cliente"
        argumentos = [cliente.id, cliente.email, cliente.nombre, cliente.apellido, cliente.telefono]
        self.__dml.procedimiento(procedimiento, argumentos)

    def baja(self, id: int):
        self.__dml.bajas_cambios(f"""
                                    DELETE FROM sgbdd.cliente 
                                    WHERE id_cliente={id}""")

    def cambio(self, cliente: Cliente):
        self.__dml.bajas_cambios(f"""
                                    UPDATE sgbdd.cliente SET 
                                    nombre_cliente='{cliente.nombre}', 
                                    email_cliente='{cliente.email}',  
                                    apellido_cliente='{cliente.apellido}', 
                                    telefono_cliente={cliente.telefono} 
                                    WHERE id_cliente={cliente.id}""")

    def consulta(self):
        encabezados = ["ID", "Nombre", "Apellido", "Email", "Telefono"]
        datos = self.__dml.consulta("""
                                    SELECT id_cliente, nombre_cliente, apellido_cliente, email_cliente, telefono_cliente
                                    FROM sgbdd.cliente""")
        return encabezados, datos

    def obten_id(self):
        id = self.__dml.consulta("SELECT sgbdd.seq_cliente.nextval FROM dual")
        return id[0][0]


if __name__ == '__main__':
    cnx = Conexion("usr_administrador", "123", "localhost/xepdb1")

    dml = DMLCliente(cnx)

    dml.baja(1)

    c = Cliente(1, "algo@hotmail.com", "Arturo", "Hernadez", "1234567890")

    dml.alta(c)

    for cat in dml.consulta():
        print(cat)

    c = Cliente(1, "otro@hotmail.com", "Juan", "Hernadez", "1234567890")
    dml.cambio(c)

    for cat in dml.consulta():
        print(cat)

    dml.baja(1)

    for cat in dml.consulta():
        print(cat)
