from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QApplication

from Controlador.Conexion import Conexion
from Vista.frm.frmderecho.FrmProducto import FrmProducto
from Vista.frm.principal.FrmPrincipalDer import FrmPrincipalDer
from Vista.frm.principal.FrmPrincipalIzq import FrmPrincipalIzq


class FrmPrincipal(QWidget):
    def __init__(self, conexion: Conexion, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = conexion

        self.layout = QHBoxLayout(self)
        self.frm_izquierdo = FrmPrincipalIzq()
        self.frm_derecho = FrmPrincipalDer(self.conexion)
        self.splitter = QSplitter(Qt.Horizontal)

        self.init_ui()
        self.set_actions()

    def init_ui(self):
        self.frm_izquierdo.setFrameShape(QFrame.StyledPanel)
        self.frm_izquierdo.setMaximumWidth(250)
        self.frm_izquierdo.setMinimumWidth(150)

        self.splitter.addWidget(self.frm_izquierdo)
        self.splitter.addWidget(self.frm_derecho)

        self.layout.addWidget(self.splitter)
        self.layout.setMargin(0)

        self.setLayout(self.layout)

    def set_actions(self) -> None:
        self.frm_izquierdo.btn_inicio.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_categoria.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_marca.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_producto.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_modo_pago.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_cliente.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_factura.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_historial_productos.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_historial_transacciones.clicked.connect(self.change_pages)
        self.frm_izquierdo.btn_salir.clicked.connect(self.regresar)

    def change_pages(self) -> None:
        if self.frm_izquierdo.btn_inicio.isChecked():
            self.frm_derecho.stack.setCurrentIndex(0)
        if self.frm_izquierdo.btn_categoria.isChecked():
            self.frm_derecho.stack.setCurrentIndex(1)
        if self.frm_izquierdo.btn_marca.isChecked():
            self.frm_derecho.stack.setCurrentIndex(2)
        if self.frm_izquierdo.btn_producto.isChecked():
            self.frm_derecho.stack.setCurrentIndex(3)
        if self.frm_izquierdo.btn_modo_pago.isChecked():
            self.frm_derecho.stack.setCurrentIndex(4)
        if self.frm_izquierdo.btn_cliente.isChecked():
            self.frm_derecho.stack.setCurrentIndex(5)
        if self.frm_izquierdo.btn_factura.isChecked():
            self.frm_derecho.stack.setCurrentIndex(6)
        if self.frm_izquierdo.btn_historial_productos.isChecked():
            self.frm_derecho.stack.setCurrentIndex(7)
        if self.frm_izquierdo.btn_historial_transacciones.isChecked():
            self.frm_derecho.stack.setCurrentIndex(8)

    def regresar(self):
        self.parent().setCurrentIndex(0)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = FrmPrincipal(Conexion("sgbdd", "123", "localhost/xepdb1"), QWidget())
    ex.show()
    sys.exit(app.exec_())
