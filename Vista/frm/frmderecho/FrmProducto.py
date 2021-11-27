from PySide2.QtWidgets import QTabWidget

from Vista.frm.frmderecho.altas.AltaProducto import AltaProducto
from Vista.frm.frmderecho.bajas.BajaProducto import BajaProducto
from Vista.frm.frmderecho.cambios.CambioProducto import CambioProducto
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmProducto(QTabWidget):
    def __init__(self):
        super().__init__()
        self.alta = AltaProducto()
        self.baja = BajaProducto()
        self.cambio = CambioProducto()
        self.consulta = Consulta(["ID", "Nombre", "Precio", "Stock", "Categoria", "Marca"], [])

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
