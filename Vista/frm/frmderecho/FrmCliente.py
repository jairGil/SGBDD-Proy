from PySide2.QtWidgets import QTabWidget, QWidget

from Controlador.DMLCliente import DMLCliente
from Modelo.Cliente import Cliente
from Vista.dlg.DlgAviso import DlgAviso
from Vista.frm.frmderecho.altas.AltaCliente import AltaCliente
from Vista.frm.frmderecho.bajas.BajaCliente import BajaCliente
from Vista.frm.frmderecho.cambios.CambioCliente import CambioCliente
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmCliente(QTabWidget):
    __dlg_aviso: DlgAviso

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = self.parent().conexion
        self.dml = DMLCliente(self.conexion)

        self.alta = AltaCliente()
        self.baja = BajaCliente()
        self.cambio = CambioCliente()
        self.consulta = Consulta()

        self.setup_ui()
        self.agrega_items()
        self.agrega_acciones_btn()
        self.agrega_acciones_cmbx()

    def setup_ui(self):
        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")

    def agrega_items(self):
        encabezados, datos = self.dml.consulta()
        self.cambio.cmbx_cliente_cambio.addItem("")
        self.baja.cmbx_cliente_baja.addItem("")
        if datos and encabezados:
            self.consulta.agrega_items(encabezados, datos)
            self.baja.cmbx_cliente_baja.setItemText(0, "Seleccione una opcion")
            self.cambio.cmbx_cliente_cambio.setItemText(0, "Seleccione una opcion")
            for reg in datos:
                cliente = Cliente(id=reg[0], nombre=reg[1], apellido=reg[2], email=reg[3], telefono=reg[4])
                self.baja.cmbx_cliente_baja.addItem(str(cliente), cliente)
                self.cambio.cmbx_cliente_cambio.addItem(str(cliente), cliente)

    def agrega_acciones_cmbx(self):
        self.baja.cmbx_cliente_baja.currentIndexChanged.connect(self.baja.agregar_datos)
        self.cambio.cmbx_cliente_cambio.currentIndexChanged.connect(self.cambio.agregar_datos)

    def agrega_acciones_btn(self):
        self.alta.btn_agregar_alta.clicked.connect(self.insertar_db)
        self.baja.btn_eliminar_baja.clicked.connect(self.eliminar_db)
        self.cambio.btn_modificar_cambio.clicked.connect(self.modificar_db)

    def insertar_db(self):
        nombre = self.alta.txt_nombre_alta.text()
        apellido = self.alta.txt_apellido_alta.text()
        email = self.alta.txt_email_alta.text()
        telefono = self.alta.txt_telefono_alta.text()

        if nombre and apellido and email and telefono:
            id = self.dml.obten_id()
            cliente = Cliente(id=id, nombre=nombre, apellido=apellido, email=email, telefono=telefono)
            self.dml.alta(cliente)
            self.alta.limpiar_campos()
            self.baja.cmbx_cliente_baja.addItem(str(cliente), cliente)
            self.cambio.cmbx_cliente_cambio.addItem(str(cliente), cliente)
            self.__dlg_aviso = DlgAviso(self, "Registro agregado correctamente.")
            self.actualiza_tabla()
        else:
            if not (nombre or apellido or email or telefono):
                self.__dlg_aviso = DlgAviso(self, "ERROR: Los campos solicitados se encuentran vacíos")
            elif not nombre:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo nombre está vacío")
            elif not apellido:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo apellido está vacío")
            elif not email:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo email está vacío")
            else:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo telefono está vacío")

    def eliminar_db(self):
        index = self.baja.cmbx_cliente_baja.currentIndex()
        if index:
            id = int(self.baja.txt_id_baja.text())
            self.dml.baja(id)
            self.baja.cmbx_cliente_baja.removeItem(index)
            self.cambio.cmbx_cliente_cambio.removeItem(index)
            self.__dlg_aviso = DlgAviso(self, "Registro eliminado con exito.")
            self.actualiza_tabla()
        else:
            self.__dlg_aviso = DlgAviso(self, "Primero debe seleccionar un elemento del combo box")

    def modificar_db(self):
        index = self.cambio.cmbx_mpago_cambio.currentIndex()
        nombre = self.cambio.txt_nombre_cambio.text()
        apellido = self.cambio.txt_apellido_cambio.text()
        email = self.cambio.txt_email_cambio.text()
        telefono = self.cambio.txt_telefono_cambio.text()

        if index:
            if nombre and apellido and email and telefono:
                cliente = self.cambio.cmbx_cliente_cambio.itemData(index)
                cliente.nombre = nombre
                cliente.apellido = apellido
                cliente.email = email
                cliente.telefono = telefono

                self.dml.cambio(cliente)

                self.cambio.cmbx_cliente_cambio.setItemText(index, str(cliente))
                self.cambio.cmbx_cliente_cambio.setItemData(index, cliente)

                self.baja.cmbx_cliente_baja.setItemText(index, str(cliente))
                self.baja.cmbx_cliente_baja.setItemData(index, cliente)

                self.cambio.cmbx_cliente_cambio.setCurrentIndex(0)
                self.cambio.limpiar_campos()
                self.__dlg_aviso = DlgAviso(self, "Registro modificado correctamente")
                self.actualiza_tabla()
            else:
                if not (nombre or apellido or email or telefono):
                    self.__dlg_aviso = DlgAviso(self, "ERROR: Los campos solicitados están vacíos")
                elif not nombre:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo nombre está vacío")
                elif not email:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo email está vacío")
                elif not telefono:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo telefono está vacío")
        else:
            self.__dlg_aviso = DlgAviso(self, "ERROR: Seleccione un registro")

    def actualiza_tabla(self):
        encabezados, datos = self.dml.consulta()
        self.consulta.agrega_items(encabezados, datos)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmCliente()
    w.show()
    sys.exit(app.exec_())
