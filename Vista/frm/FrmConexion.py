from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QStackedWidget, QSpacerItem, \
    QSizePolicy
from Controlador.Conexion import Conexion
from Vista.dlg.DlgAviso import DlgAviso


class FrmConexion(QWidget):
    __con: Conexion
    __dlg_aviso: DlgAviso
    estado_con: int

    def __init__(self, p: QStackedWidget):
        super().__init__(parent=p)
        self.layout = QGridLayout(self)
        self.lbl_usuario = QLabel("Usuario", self)
        self.txt_usuario = QLineEdit(self)
        self.lbl_contrasena = QLabel("Contraseña", self)
        self.txt_contrasena = QLineEdit(self)
        self.lbl_host = QLabel("Host", self)
        self.txt_host = QLineEdit(self)
        self.lbl_servicio = QLabel("Servicio", self)
        self.txt_servicio = QLineEdit(self)
        self.btn_conectar = QPushButton("Conectar", self)

        self.setup_ui()

    def setup_ui(self):
        self.txt_contrasena.setEchoMode(QLineEdit.Password)
        self.txt_usuario.setMinimumWidth(300)

        self.layout.addWidget(self.lbl_usuario, 1, 1)
        self.layout.addWidget(self.txt_usuario, 1, 2, 1, 2)
        self.layout.addWidget(self.lbl_contrasena, 2, 1)
        self.layout.addWidget(self.txt_contrasena, 2, 2, 1, 2)
        self.layout.addWidget(self.lbl_host, 3, 1)
        self.layout.addWidget(self.txt_host, 3, 2, 1, 2)
        self.layout.addWidget(self.lbl_servicio, 4, 1)
        self.layout.addWidget(self.txt_servicio, 4, 2, 1, 2)
        self.layout.addWidget(self.btn_conectar, 5, 2, 1, 2)

        self.layout.addItem(QSpacerItem(20, 40, vData=QSizePolicy.Expanding), 0, 1)
        self.layout.addItem(QSpacerItem(20, 40, vData=QSizePolicy.Expanding), 6, 1)
        self.layout.addItem(QSpacerItem(40, 20, hData=QSizePolicy.Expanding), 1, 0)
        self.layout.addItem(QSpacerItem(40, 20, hData=QSizePolicy.Expanding), 1, 4)

        self.btn_conectar.clicked.connect(self.conectar)

    def conectar(self):
        usuario = self.txt_usuario.text()
        contrasena = self.txt_contrasena.text()
        dsn = f"{self.txt_host.text()}/{self.txt_servicio.text()}"
        self.__con = Conexion(usuario, contrasena, dsn)

        self.estado_con, conexion_error = self.__con.conectar()
        if self.estado_con == 1:
            print("conectado")
            print(conexion_error.username)
            print(conexion_error.tag)
            self.parent().parent().set_conexion(self.__con)
        elif self.estado_con == -1:
            s = f"Error de Conexion \n\n{conexion_error}"
            self.__dlg_aviso = DlgAviso(s)
        elif self.estado_con == -2:
            s = f"Error de Base de datos \n\n{conexion_error}"
            self.__dlg_aviso = DlgAviso(s)


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = QStackedWidget()
    frm2 = FrmConexion(frm)
    frm.addWidget(frm2)
    frm.show()
    sys.exit(app.exec_())
