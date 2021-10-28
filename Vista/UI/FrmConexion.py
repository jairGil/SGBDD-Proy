from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton
from PySide2.QtWidgets import QSpacerItem, QSizePolicy, QDesktopWidget
from Controlador.Conexion import Conexion


class FrmConexion(QMainWindow):
    __con: Conexion

    def __init__(self):
        super().__init__()
        self.central_widget = QWidget(self)
        self.form_layout = QFormLayout(self.central_widget)
        self.lbl_usuario = QLabel(self.central_widget)
        self.txt_usuario = QLineEdit(self.central_widget)
        self.lbl_contrasena = QLabel(self.central_widget)
        self.txt_contrasena = QLineEdit(self.central_widget)
        self.lbl_dsn = QLabel(self.central_widget)
        self.txt_dsn = QLineEdit(self.central_widget)
        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_conectar = QPushButton(self.central_widget)
        self.lbl_estado = QLabel(self.central_widget)

        self.setup_ui()

    def setup_ui(self):
        self.resize(425, 272)

        self.txt_contrasena.setEchoMode(QLineEdit.Password)

        self.form_layout.setWidget(0, QFormLayout.LabelRole, self.lbl_usuario)
        self.form_layout.setWidget(0, QFormLayout.FieldRole, self.txt_usuario)
        self.form_layout.setWidget(2, QFormLayout.LabelRole, self.lbl_contrasena)
        self.form_layout.setWidget(2, QFormLayout.FieldRole, self.txt_contrasena)
        self.form_layout.setWidget(3, QFormLayout.LabelRole, self.lbl_dsn)
        self.form_layout.setWidget(3, QFormLayout.FieldRole, self.txt_dsn)
        self.form_layout.setWidget(4, QFormLayout.FieldRole, self.btn_conectar)
        self.form_layout.setItem(5, QFormLayout.FieldRole, self.vertical_spacer)
        self.form_layout.setWidget(6, QFormLayout.FieldRole, self.lbl_estado)

        self.setCentralWidget(self.central_widget)
        self.btn_conectar.clicked.connect(self.conectar)
        self.retranslate_ui()
        self.centrar_ventana()

    def retranslate_ui(self):
        self.setWindowTitle("Conexion")
        self.lbl_usuario.setText("Usuario")
        self.lbl_contrasena.setText("Contraseña")
        self.lbl_dsn.setText("DSN")
        self.btn_conectar.setText("Conectar")
        self.lbl_estado.setText("Estado: Desconectado")

    def conectar(self):
        usuario = self.txt_usuario.text()
        contrasena = self.txt_contrasena.text()
        dsn = self.txt_dsn.text()
        self.__con = Conexion(usuario, contrasena, dsn)

        self.lbl_estado.setText(f"Estado: {self.__con.conectar()}")

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
    mw = FrmConexion()
    mw.show()
    sys.exit(app.exec_())
