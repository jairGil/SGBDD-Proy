import PySide2.QtWidgets
from PySide2.QtWidgets import QFrame, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy


class FrmPrincipalDerecho(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.btn_inicio = QPushButton("Inicio", self)
        self.btn_categoria = QPushButton("Categoria", self)
        self.btn_marca = QPushButton("Marca", self)
        self.btn_producto = QPushButton("Producto", self)
        self.btn_modo_pago = QPushButton("Modo Pago", self)
        self.btn_cliente = QPushButton("Cliente", self)
        self.btn_factura = QPushButton("Factura", self)
        self.btn_detalle = QPushButton("Detalle", self)
        self.btn_salir = QPushButton("Salir", self)
        self.spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.layout.addWidget(self.btn_inicio)
        self.layout.addWidget(self.btn_categoria)
        self.layout.addWidget(self.btn_marca)
        self.layout.addWidget(self.btn_producto)
        self.layout.addWidget(self.btn_modo_pago)
        self.layout.addWidget(self.btn_cliente)
        self.layout.addWidget(self.btn_factura)
        self.layout.addWidget(self.btn_detalle)
        self.layout.addItem(self.spacer)
        self.layout.addWidget(self.btn_salir)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication, QWidget
    app = QApplication(sys.argv)
    wd = FrmPrincipalDerecho()
    wd.show()
    sys.exit(app.exec_())
