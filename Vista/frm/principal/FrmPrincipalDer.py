from PySide2.QtCore import Qt
from PySide2.QtWidgets import QFrame, QGridLayout, QSpacerItem, QSizePolicy, QStackedWidget, QLabel
from Vista.frm.frmderecho.FrmCategoria import FrmCategoria
from Vista.frm.frmderecho.FrmCliente import FrmCliente
from Vista.frm.frmderecho.FrmFactura import FrmFactura
from Vista.frm.frmderecho.FrmHistorialPrecio import FrmHistorialPrecio
from Vista.frm.frmderecho.FrmHistorialProducto import FrmHistorialProducto
from Vista.frm.frmderecho.FrmMarca import FrmMarca
from Vista.frm.frmderecho.FrmModoPago import FrmModoPago
from Vista.frm.frmderecho.FrmProducto import FrmProducto


class FrmPrincipalDer(QFrame):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.stack = QStackedWidget(self)
        self.frm_categoria = FrmCategoria()
        self.frm_marca = FrmMarca()
        self.frm_producto = FrmProducto()
        self.frm_modo_pago = FrmModoPago()
        self.frm_cliente = FrmCliente()
        self.frm_factura = FrmFactura()
        self.frm_historial_producto = FrmHistorialProducto()
        self.frm_historial_precio = FrmHistorialPrecio()

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
                            QFrame{
                                background-color: rgb(255, 255, 255);
                            }
                            QPushButton#btn_azul {
                                background-color: #0097A7;
                                color: #E0F7FA;
                            }
                            QPushButton#btn_rojo {
                                background-color: #B71C1C;
                                color: #FFEBEE;
                            }""")

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
        self.stack.addWidget(self.frm_modo_pago)
        self.stack.addWidget(self.frm_cliente)
        self.stack.addWidget(self.frm_factura)
        self.stack.addWidget(self.frm_historial_producto)
        self.stack.addWidget(self.frm_historial_precio)


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = FrmPrincipalDer()
    frm.show()
    sys.exit(app.exec_())
