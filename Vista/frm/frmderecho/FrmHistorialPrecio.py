from PySide2.QtWidgets import QWidget, QGridLayout
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmHistorialPrecio(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.consulta = Consulta(["ID", "Marca"], [(1, "Algo"), (2, "otro")])

        self.setup_ui()

    def setup_ui(self):
        self.layout.addWidget(self.consulta)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmHistorialPrecio()
    w.show()
    sys.exit(app.exec_())
