from PySide2.QtWidgets import QWidget, QGridLayout

from Controlador.DMLHistorialTransacciones import DMLHistorialTransacciones
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmHistorialTransacciones(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = self.parent().conexion
        self.dml = DMLHistorialTransacciones(self.conexion)
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
    w = FrmHistorialTransacciones()
    w.show()
    sys.exit(app.exec_())
