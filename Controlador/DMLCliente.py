from Modelo.Cliente import Cliente
from DML import *


class DMLCliente:

    @SQLABC(conexion=cnx)
    def alta(self, cliente: Cliente):
        return f"""INSERT INTO cliente(id_cliente, email_cliente, nombre_cliente, apellido_cliente, telefono_cliente) 
                VALUES ({cliente.id},'{cliente.email}', '{cliente.nombre}', '{cliente.apellido}', {cliente.telefono})"""

    @SQLABC(conexion=cnx)
    def baja(self, id: int):
        return f"""DELETE FROM cliente 
                   WHERE id_cliente={id}"""

    @SQLABC(conexion=cnx)
    def cambio(self, cliente: Cliente):
        return f"""UPDATE cliente SET 
                   nombre_cliente='{cliente.nombre}', 
                   email_cliente='{cliente.email}',  
                   apellido_cliente='{cliente.apellido}', 
                   telefono_cliente={cliente.telefono} 
                   WHERE id_cliente={cliente.id}"""

    @SQLC(conexion=cnx)
    def consulta(self):
        return "SELECT * FROM cliente"


if __name__ == '__main__':

    dml = DMLCliente()

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
