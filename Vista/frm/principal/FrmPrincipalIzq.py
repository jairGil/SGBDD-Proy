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
        self.btn_historial_productos = QPushButton("Historial Productos", self)
        self.btn_historial_precios = QPushButton("Historial Precios", self)
        self.btn_salir = QPushButton("Salir", self)
        self.spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)

        self.botones = [self.btn_inicio, self.btn_categoria, self.btn_marca, self.btn_producto, self.btn_modo_pago,
                        self.btn_cliente, self.btn_factura, self.btn_historial_productos, self.btn_historial_precios]

        self.setup_ui()

    def setup_ui(self):
        self.layout.setMargin(0)

        for b in self.botones:
            self.layout.addWidget(b)

        self.layout.addItem(self.spacer)
        self.layout.addWidget(self.btn_salir)

        for b in self.botones:
            b.setAutoExclusive(True)

        for b in self.botones:
            b.setCheckable(True)

        self.btn_inicio.setChecked(True)

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
