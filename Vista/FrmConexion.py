from PySide2.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QPushButton
from PySide2.QtWidgets import QSpacerItem, QSizePolicy
from Controlador.Conexion import Conexion
from Vista.DlgAviso import DlgAviso


class FrmConexion(QWidget):
    __con: Conexion
    __dlg_aviso: DlgAviso
    estado_con: int

    def __init__(self):
        super().__init__()
        self.form_layout = QFormLayout(self)
        self.lbl_usuario = QLabel(self)
        self.txt_usuario = QLineEdit(self)
        self.lbl_contrasena = QLabel(self)
        self.txt_contrasena = QLineEdit(self)
        self.lbl_ip = QLabel(self)
        self.txt_ip = QLineEdit(self)
        self.lbl_servicio = QLabel(self)
        self.txt_servicio = QLineEdit(self)
        self.btn_conectar = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        self.txt_contrasena.setEchoMode(QLineEdit.Password)

        self.form_layout.setWidget(0, QFormLayout.LabelRole, self.lbl_usuario)
        self.form_layout.setWidget(0, QFormLayout.FieldRole, self.txt_usuario)
        self.form_layout.setWidget(1, QFormLayout.LabelRole, self.lbl_contrasena)
        self.form_layout.setWidget(1, QFormLayout.FieldRole, self.txt_contrasena)
        self.form_layout.setWidget(2, QFormLayout.LabelRole, self.lbl_ip)
        self.form_layout.setWidget(2, QFormLayout.FieldRole, self.txt_ip)
        self.form_layout.setWidget(3, QFormLayout.LabelRole, self.lbl_servicio)
        self.form_layout.setWidget(3, QFormLayout.FieldRole, self.txt_servicio)
        self.form_layout.setWidget(4, QFormLayout.FieldRole, self.btn_conectar)

        self.btn_conectar.clicked.connect(self.conectar)
        self.retranslate_ui()

    def retranslate_ui(self):
        self.setWindowTitle("Conexion")
        self.lbl_usuario.setText("Usuario")
        self.lbl_contrasena.setText("Contraseña")
        self.lbl_ip.setText("IP")
        self.lbl_servicio.setText("Servicio")
        self.btn_conectar.setText("Conectar")

    def conectar(self):
        usuario = self.txt_usuario.text()
        contrasena = self.txt_contrasena.text()
        dsn = f"{self.txt_ip.text()}/{self.txt_servicio.text()}"
        self.__con = Conexion(usuario, contrasena, dsn)

        self.estado_con, e = self.__con.conectar()
        if self.estado_con == 1:
            print("conectado")
            print(type(e))
        elif self.estado_con == -1:
            s = f"Error de Conexion \n\n{e}"
            self.__dlg_aviso = DlgAviso(s)
        elif self.estado_con == -2:
            s = f"Error de Base de datos \n\n{e}"
            self.__dlg_aviso = DlgAviso(s)


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication, QMainWindow
    import sys

    app = QApplication(sys.argv)
    frm = QMainWindow()
    frm.setCentralWidget(FrmConexion())
    frm.show()
    sys.exit(app.exec_())
