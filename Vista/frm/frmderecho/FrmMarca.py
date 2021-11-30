from PySide2.QtWidgets import QTabWidget, QWidget

from Controlador.DMLMarca import DMLMarca
from Modelo.Marca import Marca
from Vista.dlg.DlgAviso import DlgAviso
from Vista.frm.frmderecho.altas.AltaMarca import AltaMarca
from Vista.frm.frmderecho.bajas.BajaMarca import BajaMarca
from Vista.frm.frmderecho.cambios.CambioMarca import CambioMarca
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmMarca(QTabWidget):
    __dlg_aviso: DlgAviso

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = self.parent().conexion
        self.dml = DMLMarca(self.conexion)

        self.alta = AltaMarca()
        self.baja = BajaMarca()
        self.cambio = CambioMarca()
        self.consulta = Consulta()

        self.setup_ui()
        self.agrega_items()
        self.agrega_acciones_cmbx()
        self.agrega_acciones_btn()

    def setup_ui(self):
        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")

    def agrega_items(self):
        encabezados, datos = self.dml.consulta()
        self.baja.cmbx_marca_baja.addItem("")
        self.cambio.cmbx_marca_cambio.addItem("")
        if datos and encabezados:
            self.consulta.agrega_items(encabezados, datos)
            self.baja.cmbx_marca_baja.setItemText(0, "Seleccione una opcion")
            self.cambio.cmbx_marca_cambio.setItemText(0, "Seleccione una opcion")
            for reg in datos:
                mar = Marca(reg[0], reg[1])
                self.baja.cmbx_marca_baja.addItem(str(mar), mar)
                self.cambio.cmbx_marca_cambio.addItem(str(mar), mar)

    def agrega_acciones_cmbx(self):
        self.baja.cmbx_marca_baja.currentIndexChanged.connect(self.baja.agregar_datos)
        self.cambio.cmbx_marca_cambio.currentIndexChanged.connect(self.cambio.agregar_datos)

    def agrega_acciones_btn(self):
        self.alta.btn_agregar_alta.clicked.connect(self.insertar_db)
        self.baja.btn_eliminar_baja.clicked.connect(self.eliminar_db)
        self.cambio.btn_modificar_cambio.clicked.connect(self.modificar_db)

    def insertar_db(self):
        nombre = self.alta.txt_marca_alta.text()
        if nombre:
            id = self.dml.obten_id()
            marca = Marca(id, nombre)
            print(marca)
            self.dml.alta(marca)
            self.alta.limpiar_campos()
            self.baja.cmbx_marca_baja.addItem(str(marca), marca)
            self.cambio.cmbx_marca_cambio.addItem(str(marca), marca)
            self.__dlg_aviso = DlgAviso(self, "Registro agregado correctamente.")
            self.actualiza_tabla()
        else:
            if not nombre:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo categoria está vacío")

    def eliminar_db(self):
        index = self.baja.cmbx_marca_baja.currentIndex()
        if index:
            id = int(self.baja.txt_id_baja.text())
            self.dml.baja(id)
            self.baja.cmbx_marca_baja.removeItem(index)
            self.cambio.cmbx_marca_cambio.removeItem(index)
            self.baja.cmbx_marca_baja.setCurrentIndex(0)
            self.baja.limpiar_campos()
            self.__dlg_aviso = DlgAviso(self, "Registro eliminado con exito.")
            self.actualiza_tabla()
        else:
            self.__dlg_aviso = DlgAviso(self, "Primero debe seleccionar un elemento del combo box")

    def modificar_db(self):
        index = self.cambio.cmbx_marca_cambio.currentIndex()
        nombre = self.cambio.txt_nombre_cambio.text()
        if index:
            if nombre:
                marca = self.cambio.cmbx_marca_cambio.itemData(index)
                marca.nombre = nombre

                self.cambio.cmbx_marca_cambio.setItemText(index, str(marca))
                self.cambio.cmbx_marca_cambio.setItemData(index, marca)

                self.baja.cmbx_marca_baja.setItemText(index, str(marca))
                self.baja.cmbx_marca_baja.setItemData(index, marca)

                self.dml.cambio(marca)
                self.cambio.limpiar_campos()
                self.cambio.cmbx_marca_cambio.setCurrentIndex(0)
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
        for i in range(1, self.cambio.cmbx_marca_cambio.count()):
            self.cambio.cmbx_marca_cambio.removeItem(i)
            self.baja.cmbx_marca_baja.removeItem(i)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmMarca()
    w.show()
    sys.exit(app.exec_())
