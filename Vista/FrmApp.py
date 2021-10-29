from PySide2.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QStackedWidget, QVBoxLayout

from Vista.FrmConexion import FrmConexion
from Vista.FrmPrincipal import FrmPrincipal


class FrmApp(QMainWindow):
    def __init__(self):
        super().__init__()
        super().setLayout(QVBoxLayout())
        self.stack_widget = QStackedWidget(self)
        self.pag_conexion = FrmConexion(self.stack_widget)
        self.pag_app = FrmPrincipal()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.resize(400, 100)
        self.setWindowTitle("Sistema de gestión de inventario")

        self.stack_widget.addWidget(self.pag_conexion)
        self.stack_widget.addWidget(self.pag_app)
        self.setCentralWidget(self.stack_widget)

        self.centrar_ventana()

    def centrar_ventana(self):
        # Obtener tamaño de pantalla
        pantalla = QDesktopWidget().screenGeometry()
        # Obtener el tamaño de la ventana
        ventana = self.geometry()
        # Mueva la ventana al centro de la pantalla
        self.move(int((pantalla.width() - ventana.width()) / 2), int((pantalla.height() - ventana.height()) / 2))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    frm = FrmApp()
    sys.exit(app.exec_())
