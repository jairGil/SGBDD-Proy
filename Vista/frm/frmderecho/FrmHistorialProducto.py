from PySide2.QtWidgets import QWidget, QGridLayout

from Controlador.DMLHistorialProducto import DMLHistorialProducto
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmHistorialProducto(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = self.parent().conexion
        self.dml = DMLHistorialProducto(self.conexion)

        self.layout = QGridLayout(self)
        self.consulta = Consulta()

        self.setup_ui()
        self.agrega_items()

    def setup_ui(self):
        self.layout.addWidget(self.consulta)

    def agrega_items(self):
        encabezados, datos = self.dml.consulta()
        if datos and encabezados:
            self.consulta.agrega_items(encabezados, datos)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmHistorialProducto()
    w.show()
    sys.exit(app.exec_())
