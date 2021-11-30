from PySide2.QtWidgets import QTabWidget, QWidget

from Controlador.DMLProducto import DMLProducto
from Vista.dlg.DlgAviso import DlgAviso
from Vista.frm.frmderecho.altas.AltaProducto import AltaProducto
from Vista.frm.frmderecho.bajas.BajaProducto import BajaProducto
from Vista.frm.frmderecho.cambios.CambioProducto import CambioProducto
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmProducto(QTabWidget):
    __dlg_aviso: DlgAviso

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = self.parent().conexion
        self.dml = DMLProducto(self.conexion)

        self.alta = AltaProducto()
        self.baja = BajaProducto()
        self.cambio = CambioProducto()
        self.consulta = Consulta()

        self.setup_ui()

    def setup_ui(self):
        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmProducto()
    w.show()
    sys.exit(app.exec_())
