from PySide2.QtWidgets import QTabWidget

from Vista.frm.frmderecho.altas.AltaModoPago import AltaModoPago
from Vista.frm.frmderecho.bajas.BajaModoPago import BajaModoPago
from Vista.frm.frmderecho.cambios.CambioModoPago import CambioModoPago
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmModoPago(QTabWidget):
    def __init__(self):
        super().__init__()
        self.alta = AltaModoPago()
        self.baja = BajaModoPago()
        self.cambio = CambioModoPago()
        self.consulta = Consulta(["ID", "Modo Pago", "Detalles"],
                                 [(1, "Efectivo", "Pagos en efectivo"), (2, "Transferencia", "Pagos por transferencia")])

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
    w = FrmModoPago()
    w.show()
    sys.exit(app.exec_())
