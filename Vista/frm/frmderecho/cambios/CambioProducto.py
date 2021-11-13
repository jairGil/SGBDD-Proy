from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QSpacerItem, QSizePolicy, QComboBox, QLabel, QPushButton


class CambioProducto(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_producto_cambio = QLabel("Producto", self)
        self.cmbx_producto_cambio = QComboBox(self)
        self.lbl_detalles_cambio = QLabel("Detalles", self)
        self.lbl_id_cambio = QLabel("ID", self)
        self.txt_id_cambio = QLineEdit(self)
        self.lbl_nombre_cambio = QLabel("Producto", self)
        self.txt_producto_cambio = QLineEdit(self)
        self.lbl_precio_cambio = QLabel("Precio", self)
        self.txt_precio_cambio = QLineEdit(self)
        self.lbl_stock_cambio = QLabel("Stock", self)
        self.txt_stock_cambio = QLineEdit(self)
        self.lbl_categoria_cambio = QLabel("Categoria", self)
        self.txt_categoria_cambio = QLineEdit(self)
        self.lbl_marca_cambio = QLabel("Marca", self)
        self.txt_marca_cambio = QLineEdit(self)
        self.btn_cancelar_cambio = QPushButton("Cancelar", self)
        self.btn_modificar_cambio = QPushButton("Modificar", self)

        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.cmbx_producto_cambio.setMinimumSize(250, 0)
        self.txt_id_cambio.setEnabled(False)

        self.layout.addWidget(self.lbl_producto_cambio, 1, 1)
        self.layout.addWidget(self.cmbx_producto_cambio, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_detalles_cambio, 2, 1)

        self.layout.addWidget(self.lbl_id_cambio, 3, 1)
        self.layout.addWidget(self.txt_id_cambio, 3, 2, 1, 2)

        self.layout.addWidget(self.lbl_nombre_cambio, 4, 1)
        self.layout.addWidget(self.txt_producto_cambio, 4, 2, 1, 2)

        self.layout.addWidget(self.lbl_precio_cambio, 5, 1)
        self.layout.addWidget(self.txt_precio_cambio, 5, 2, 1, 2)

        self.layout.addWidget(self.lbl_stock_cambio, 6, 1)
        self.layout.addWidget(self.txt_stock_cambio, 6, 2, 1, 2)

        self.layout.addWidget(self.lbl_categoria_cambio, 7, 1)
        self.layout.addWidget(self.txt_categoria_cambio, 7, 2, 1, 2)

        self.layout.addWidget(self.lbl_marca_cambio, 8, 1)
        self.layout.addWidget(self.txt_marca_cambio, 8, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_cambio, 10, 2)
        self.layout.addWidget(self.btn_modificar_cambio, 10, 3)

        self.layout.addItem(self.v_spacer, 0, 1)
        self.layout.addItem(self.v_spacer_2, 9, 1)
        self.layout.addItem(self.v_spacer_3, 11, 1)
        self.layout.addItem(self.h_spacer, 1, 0)
        self.layout.addItem(self.h_spacer_2, 1, 4)

        self.btn_cancelar_cambio.setObjectName(u"btn_cancelar_cambio")
        self.btn_modificar_cambio.setObjectName(u"btn_modificar_cambio")
