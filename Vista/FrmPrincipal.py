from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QFrame, QTextEdit, QSplitter, QApplication

from Vista.FrmPrincipalDerecho import FrmPrincipalDerecho


class FrmPrincipal(QWidget):
    def __init__(self):
        super(FrmPrincipal, self).__init__()
        self.layout = QHBoxLayout(self)
        self.frm_izquierdo = FrmPrincipalDerecho()
        self.frm_derecho = QTextEdit()
        self.splitter = QSplitter(Qt.Horizontal)
        self.init_ui()

    def init_ui(self):
        self.frm_izquierdo.setFrameShape(QFrame.StyledPanel)
        self.frm_izquierdo.setMaximumWidth(250)
        self.frm_izquierdo.setMinimumWidth(90)

        self.splitter.addWidget(self.frm_izquierdo)
        self.splitter.addWidget(self.frm_derecho)

        self.layout.addWidget(self.splitter)
        self.layout.setMargin(0)

        self.setLayout(self.layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = FrmPrincipal()
    sys.exit(app.exec_())
