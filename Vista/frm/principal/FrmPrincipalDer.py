from PySide2.QtCore import Qt
from PySide2.QtWidgets import QFrame, QGridLayout, QSpacerItem, QSizePolicy, QStackedWidget, QLabel
from Vista.frm.frmderecho.FrmCategoria import FrmCategoria
from Vista.frm.frmderecho.FrmMarca import FrmMarca
from Vista.frm.frmderecho.FrmProducto import FrmProducto


class FrmPrincipalDer(QFrame):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.stack = QStackedWidget(self)
        self.frm_categoria = FrmCategoria()
        self.frm_marca = FrmMarca()
        self.frm_producto = FrmProducto()

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("QFrame{background-color: #ECEFF1;}")

        self.grid_layout.addItem(QSpacerItem(20, 5, vData=QSizePolicy.Minimum), 0, 1)
        self.grid_layout.addItem(QSpacerItem(20, 5, vData=QSizePolicy.Minimum), 2, 1)
        self.grid_layout.addItem(QSpacerItem(5, 5, hData=QSizePolicy.Expanding), 1, 0)
        self.grid_layout.addItem(QSpacerItem(5, 20, hData=QSizePolicy.Expanding), 1, 2)
        self.grid_layout.addWidget(self.stack, 1, 1)

        self.stack.setMinimumSize(900, 600)
        lbl = QLabel("Aqui estoy", self.stack)
        lbl.setAlignment(Qt.AlignCenter)
        self.stack.addWidget(lbl)
        self.stack.addWidget(self.frm_categoria)
        self.stack.addWidget(self.frm_marca)
        self.stack.addWidget(self.frm_producto)


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = FrmPrincipalDer()
    frm.show()
    sys.exit(app.exec_())
