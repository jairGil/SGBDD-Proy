from PySide2.QtWidgets import QTabWidget

from Vista.frm.frmderecho.altas.AltaMarca import AltaMarca
from Vista.frm.frmderecho.bajas.BajaMarca import BajaMarca
from Vista.frm.frmderecho.cambios.CambioMarca import CambioMarca
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmMarca(QTabWidget):
    def __init__(self):
        super().__init__()
        self.alta = AltaMarca()
        self.baja = BajaMarca()
        self.cambio = CambioMarca()
        self.consulta = Consulta(["ID", "Marca"], [(1, "Algo"), (2, "otro")])

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
    w = FrmMarca()
    w.show()
    sys.exit(app.exec_())