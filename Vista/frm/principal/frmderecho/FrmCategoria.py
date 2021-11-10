from PySide2.QtCore import QMetaObject, QCoreApplication
from PySide2.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QFrame, QAbstractItemView, \
    QTabWidget

from Vista.frm.principal.frmderecho.altas.AltaCategoria import AltaCategoria
from Vista.frm.principal.frmderecho.bajas.BajaCategoria import BajaCategoria
from Vista.frm.principal.frmderecho.cambios.CambioCategoria import CambioCategoria
from Vista.frm.principal.frmderecho.consultas.ConsultaCategoria import ConsultaCategoria


class FrmCategoria(QTabWidget):
    def __init__(self):
        super().__init__()
        self.alta = AltaCategoria()
        self.baja = BajaCategoria()

        self.cambio = CambioCategoria()

        self.consulta = ConsultaCategoria()

        self.setup_ui()

    def setup_ui(self):
        self.resize(569, 450)
        self.setStyleSheet(u"QPushButton#btn_agregar_alta, \n"
                           "#btn_modificar_cambio, \n"
                           "#btn_cancelar_baja {\n"
                           "	background-color: #0097A7;\n"
                           "	color: #E0F7FA;\n"
                           "}\n"
                           "QPushButton#btn_cancelar_alta, \n"
                           "#btn_cancelar_cambio,\n"
                           "#btn_eliminar_baja {\n"
                           "	background-color: #B71C1C;\n"
                           "	color: #FFEBEE;\n"
                           "}")

        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmCategoria()
    w.show()
    sys.exit(app.exec_())
