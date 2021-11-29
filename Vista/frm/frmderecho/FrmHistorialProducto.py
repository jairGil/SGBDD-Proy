from PySide2.QtWidgets import QWidget, QGridLayout
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmHistorialProducto(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.consulta = Consulta()

        self.setup_ui()

    def setup_ui(self):
        self.layout.addWidget(self.consulta)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmHistorialProducto()
    w.show()
    sys.exit(app.exec_())
