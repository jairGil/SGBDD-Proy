from PySide2.QtWidgets import QTabWidget

from Vista.frm.frmderecho.altas.AltaCliente import AltaCliente
from Vista.frm.frmderecho.bajas.BajaCliente import BajaCliente
from Vista.frm.frmderecho.cambios.CambioCliente import CambioCliente
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmCliente(QTabWidget):
    def __init__(self):
        super().__init__()
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


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmCliente()
    w.show()
    sys.exit(app.exec_())
