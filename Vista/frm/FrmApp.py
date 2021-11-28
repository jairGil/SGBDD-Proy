from PySide2.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QStackedWidget, QVBoxLayout

from Controlador.Conexion import Conexion
from Vista.frm.FrmConexion import FrmConexion
from Vista.frm.principal.FrmPrincipal import FrmPrincipal


class FrmApp(QMainWindow):
    def __init__(self):
        super().__init__()
        super().setLayout(QVBoxLayout())
        self.stack_widget = QStackedWidget(self)
        self.frm_conexion = FrmConexion(self.stack_widget)
        self.frm_principal = None
        self.conexion = None
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.setWindowTitle("Sistema de gestión de inventario")
        self.setStyleSheet("QFrame{background-color: #ECEFF1;}")

        self.stack_widget.addWidget(self.frm_conexion)
        self.setCentralWidget(self.stack_widget)

        self.centrar_ventana()

    def centrar_ventana(self):
        # Obtener tamaño de pantalla
        pantalla = QDesktopWidget().screenGeometry()
        # Obtener el tamaño de la ventana
        ventana = self.geometry()
        # Mueva la ventana al centro de la pantalla
        self.move(int((pantalla.width() - ventana.width()) / 2), int((pantalla.height() - ventana.height()) / 2))

    def set_conexion(self, conexion: Conexion):
        self.conexion = conexion
        self.frm_principal = FrmPrincipal(self.conexion, self.stack_widget)
        self.stack_widget.addWidget(self.frm_principal)
        self.stack_widget.setCurrentIndex(1)
        self.centrar_ventana()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    frm = FrmApp()
    sys.exit(app.exec_())
