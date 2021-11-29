from PySide2.QtWidgets import QTabWidget, QWidget

from Controlador.DMLCategoria import DMLCategoria
from Vista.frm.frmderecho.altas.AltaCategoria import AltaCategoria
from Vista.frm.frmderecho.bajas.BajaCategoria import BajaCategoria
from Vista.frm.frmderecho.cambios.CambioCategoria import CambioCategoria
from Vista.frm.frmderecho.consultas.Consulta import Consulta

from Modelo.Categoria import Categoria


class FrmCategoria(QTabWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = self.parent().conexion
        self.dml = DMLCategoria(self.conexion)

        self.alta = AltaCategoria()
        self.baja = BajaCategoria()
        self.cambio = CambioCategoria()
        self.consulta = Consulta()

        self.setup_ui()
        self.agrega_items()
        self.agrega_acciones_cmbx()

    def setup_ui(self):
        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")

    def agrega_items(self):
        encabezados, datos = self.dml.consulta()
        if datos and encabezados:
            self.consulta.agrega_items(encabezados, datos)
            self.baja.cmbx_categoria_baja.addItem("")
            self.cambio.cmbx_categoria_cambio.addItem("")
            for reg in datos:
                cat = Categoria(reg[0], reg[1], reg[2])
                self.baja.cmbx_categoria_baja.addItem(str(cat), cat)
                self.cambio.cmbx_categoria_cambio.addItem(str(cat), cat)

    def agrega_acciones_cmbx(self):
        self.baja.cmbx_categoria_baja.currentTextChanged.connect(self.baja.agregar_datos)
        # self.cambio.cmbx_categoria_cambio.currentIndexChanged.connect()


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmCategoria()
    w.show()
    sys.exit(app.exec_())
