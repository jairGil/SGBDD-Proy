from PySide2.QtWidgets import QTabWidget

from Vista.frm.frmderecho.altas.AltaCategoria import AltaCategoria
from Vista.frm.frmderecho.bajas.BajaCategoria import BajaCategoria
from Vista.frm.frmderecho.cambios.CambioCategoria import CambioCategoria
from Vista.frm.frmderecho.consultas.ConsultaCategoria import ConsultaCategoria


class FrmCategoria(QTabWidget):
    def __init__(self):
        super().__init__()
        self.alta = AltaCategoria()
        self.baja = BajaCategoria()
        self.cambio = CambioCategoria()
        self.consulta = ConsultaCategoria()

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""QPushButton#btn_agregar_alta,
                               #btn_modificar_cambio,
                               #btn_cancelar_baja {
                               background-color: #0097A7;
                               color: #E0F7FA;
                               }
                               QPushButton#btn_cancelar_alta, 
                               #btn_cancelar_cambio,
                               #btn_eliminar_baja {
                               background-color: #B71C1C;
                               color: #FFEBEE;
                           }""")

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
