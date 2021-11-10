from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton


class DlgAviso(QDialog):
    def __init__(self, s: str):
        super().__init__()
        self.gridLayout = QGridLayout(self)
        self.lbl_error = QLabel(s, self)
        self.btn_cerrar = QPushButton("Cerrar", self)

        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.resize(350, 250)
        self.setWindowTitle("Informe")
        self.lbl_error.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.lbl_error.setWordWrap(True)
        self.lbl_error.setMargin(30)

        self.setStyleSheet("""
                              QWidget {
                                  background-color: white;
                              }
                                        
                              QPushButton {
                                  color: white;
                                  background-color: rgb(200, 0, 0);
                                  height: 40;
                              }""")

        font = QFont()
        font.setBold(True)
        font.setWeight(11)
        font.setFamily("Cantarell")
        self.btn_cerrar.setFont(font)

        self.gridLayout.addWidget(self.lbl_error, 0, 0)
        self.gridLayout.addWidget(self.btn_cerrar, 1, 0)

        self.btn_cerrar.clicked.connect(self.cerrar_dlg)

    def cerrar_dlg(self):
        self.close()


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication, QMainWindow
    import sys

    app = QApplication(sys.argv)
    frm = QMainWindow()
    frm.show()
    st = "Este es un mensaje de prueba del texto de la ventana"
    dlg = DlgAviso(st)
    dlg.show()
    sys.exit(app.exec_())
