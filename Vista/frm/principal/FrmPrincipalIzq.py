from PySide2.QtWidgets import QFrame, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy


class FrmPrincipalIzq(QFrame):
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
        self.layout.setMargin(0)
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

        self.btn_inicio.setAutoExclusive(True)
        self.btn_categoria.setAutoExclusive(True)
        self.btn_marca.setAutoExclusive(True)
        self.btn_producto.setAutoExclusive(True)
        self.btn_modo_pago.setAutoExclusive(True)
        self.btn_cliente.setAutoExclusive(True)
        self.btn_factura.setAutoExclusive(True)
        self.btn_detalle.setAutoExclusive(True)

        self.btn_inicio.setCheckable(True)
        self.btn_categoria.setCheckable(True)
        self.btn_marca.setCheckable(True)
        self.btn_producto.setCheckable(True)
        self.btn_modo_pago.setCheckable(True)
        self.btn_cliente.setCheckable(True)
        self.btn_factura.setCheckable(True)
        self.btn_detalle.setCheckable(True)

        self.setStyleSheet("""
            QFrame {
                background-color: #00ACC1;
            }
            
            QPushButton {
                border: none;
                background-color: none;
                color: #E0F7FA;
                height: 30px;
                text-align: left;
                padding: 5px 10px 5px 10px;
            }
            
            QPushButton:hover {
                background-color: #00BCD4;
            }
            
            QPushButton:checked {
                background-color: #0097A7;
            }
        """)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    wd = FrmPrincipalIzq()
    wd.show()
    sys.exit(app.exec_())
