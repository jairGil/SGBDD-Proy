from PySide2.QtWidgets import QTabWidget, QWidget

from Controlador.DMLCliente import DMLCliente
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

    def setup_ui(self):
        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")

    def agrega_items(self):
        encabezados, datos = self.dml.consulta()
        self.cambio.cmbx_mpago_cambio.addItem("")
        self.baja.cmbx_mpago_baja.addItem("")
        if datos and encabezados:
            self.consulta.agrega_items(encabezados, datos)
            self.baja.cmbx_mpago_baja.setItemText(0, "Seleccione una opcion")
            self.cambio.cmbx_mpago_cambio.setItemText(0, "Seleccione una opcion")
            for reg in datos:
                mpago = ModoPago(reg[0], reg[1], reg[2])
                self.baja.cmbx_mpago_baja.addItem(str(mpago), mpago)
                self.cambio.cmbx_mpago_cambio.addItem(str(mpago), mpago)

    def agrega_acciones_cmbx(self):
        self.baja.cmbx_mpago_baja.currentIndexChanged.connect(self.baja.agregar_datos)
        self.cambio.cmbx_mpago_cambio.currentIndexChanged.connect(self.cambio.agregar_datos)

    def agrega_acciones_btn(self):
        self.alta.btn_agregar_alta.clicked.connect(self.insertar_db)
        self.baja.btn_eliminar_baja.clicked.connect(self.eliminar_db)
        self.cambio.btn_modificar_cambio.clicked.connect(self.modificar_db)

    def insertar_db(self):
        nombre = self.alta.txt_mpago_alta.text()
        detalle = self.alta.txt_detalles_alta.text()
        if nombre and detalle:
            id = self.dml.obten_id()
            mpago = ModoPago(id, nombre, detalle)
            self.dml.alta(mpago)
            self.alta.limpiar_campos()
            self.baja.cmbx_mpago_baja.addItem(str(mpago), mpago)
            self.cambio.cmbx_mpago_cambio.addItem(str(mpago), mpago)
            self.__dlg_aviso = DlgAviso(self, "Registro agregado correctamente.")
            self.actualiza_tabla()
        else:
            if not (nombre or detalle):
                self.__dlg_aviso = DlgAviso(self, "ERROR: Los campos solicitados se encuentran vacíos")
            elif not nombre:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo modo pago está vacío")
            else:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo detalle está vacío")

    def eliminar_db(self):
        index = self.baja.cmbx_mpago_baja.currentIndex()
        if index:
            id = int(self.baja.txt_id_baja.text())
            self.dml.baja(id)
            self.baja.cmbx_mpago_baja.removeItem(index)
            self.cambio.cmbx_mpago_cambio.removeItem(index)
            self.__dlg_aviso = DlgAviso(self, "Registro eliminado con exito.")
            self.actualiza_tabla()
        else:
            self.__dlg_aviso = DlgAviso(self, "Primero debe seleccionar un elemento del combo box")

    def modificar_db(self):
        index = self.cambio.cmbx_mpago_cambio.currentIndex()
        nombre = self.cambio.txt_nombre_cambio.text()
        detalle = self.cambio.txt_detalle_cambio.text()
        if index:
            if nombre and detalle:
                mpago = self.cambio.cmbx_mpago_cambio.itemData(index)
                mpago.nombre = nombre
                mpago.detalles = detalle

                self.cambio.cmbx_mpago_cambio.setItemText(index, str(mpago))
                self.cambio.cmbx_mpago_cambio.setItemData(index, mpago)

                self.baja.cmbx_mpago_baja.setItemText(index, str(mpago))
                self.baja.cmbx_mpago_baja.setItemData(index, mpago)

                self.dml.cambio(mpago)
                self.cambio.cmbx_mpago_cambio.setCurrentIndex(0)
                self.cambio.limpiar_campos()
                self.__dlg_aviso = DlgAviso(self, "Registro modificado correctamente")
                self.actualiza_tabla()
            else:
                if not nombre:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo categoria está vacío")
        else:
            self.__dlg_aviso = DlgAviso(self, "ERROR: Seleccione un registro")

    def actualiza_tabla(self):
        encabezados, datos = self.dml.consulta()
        self.consulta.agrega_items(encabezados, datos)

    def remueve_items_cmbx(self):
        for i in range(1, self.cambio.cmbx_mpago_cambio.count()):
            self.cambio.cmbx_mpago_cambio.removeItem(i)
            self.baja.cmbx_mpago_baja.removeItem(i)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmCliente()
    w.show()
    sys.exit(app.exec_())
