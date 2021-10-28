from PySide2.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QStackedWidget

from Vista.FrmConexion import FrmConexion


class FrmApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QStackedWidget()
        self.pag_conexion = FrmConexion()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.resize(483, 373)

        self.centralwidget.addWidget(self.pag_conexion)

        self.setCentralWidget(self.centralwidget)
        self.retranslate_ui()
        self.centrar_ventana()

    def retranslate_ui(self):
        self.setWindowTitle("Sistema de gestión de inventario")

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
