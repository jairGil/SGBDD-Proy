from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QSpacerItem, QSizePolicy, QComboBox, QLabel, QPushButton


class BajaProducto(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_producto_baja = QLabel("Producto", self)
        self.cmbx_producto_baja = QComboBox(self)
        self.lbl_detalles_baja = QLabel("Detalles", self)
        self.lbl_id_baja = QLabel("ID", self)
        self.txt_id_baja = QLineEdit(self)
        self.lbl_nombre_baja = QLabel("Producto", self)
        self.txt_producto_baja = QLineEdit(self)
        self.lbl_precio_baja = QLabel("Precio", self)
        self.txt_precio_baja = QLineEdit(self)
        self.lbl_stock_baja = QLabel("Stock", self)
        self.txt_stock_baja = QLineEdit(self)
        self.lbl_categoria_baja = QLabel("Categoria", self)
        self.txt_categoria_baja = QLineEdit(self)
        self.lbl_marca_baja = QLabel("Marca", self)
        self.txt_marca_baja = QLineEdit(self)
        self.btn_cancelar_baja = QPushButton("Cancelar", self)
        self.btn_eliminar_baja = QPushButton("Eliminar", self)

        self.txts = [self.txt_id_baja, self.txt_producto_baja, self.txt_precio_baja, self.txt_stock_baja,
                     self.txt_categoria_baja, self.txt_marca_baja]

        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.cmbx_producto_baja.setMinimumSize(250, 0)

        for txt in self.txts:
            txt.setEnabled(False)

        self.layout.addWidget(self.lbl_producto_baja, 1, 1)
        self.layout.addWidget(self.cmbx_producto_baja, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_detalles_baja, 2, 1)

        self.layout.addWidget(self.lbl_id_baja, 3, 1)
        self.layout.addWidget(self.txt_id_baja, 3, 2, 1, 2)

        self.layout.addWidget(self.lbl_nombre_baja, 4, 1)
        self.layout.addWidget(self.txt_producto_baja, 4, 2, 1, 2)

        self.layout.addWidget(self.lbl_precio_baja, 5, 1)
        self.layout.addWidget(self.txt_precio_baja, 5, 2, 1, 2)

        self.layout.addWidget(self.lbl_stock_baja, 6, 1)
        self.layout.addWidget(self.txt_stock_baja, 6, 2, 1, 2)

        self.layout.addWidget(self.lbl_categoria_baja, 7, 1)
        self.layout.addWidget(self.txt_categoria_baja, 7, 2, 1, 2)

        self.layout.addWidget(self.lbl_marca_baja, 8, 1)
        self.layout.addWidget(self.txt_marca_baja, 8, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_baja, 10, 2)
        self.layout.addWidget(self.btn_eliminar_baja, 10, 3)

        self.layout.addItem(self.v_spacer, 0, 0)
        self.layout.addItem(self.v_spacer_2, 9, 1)
        self.layout.addItem(self.v_spacer_3, 11, 1)
        self.layout.addItem(self.h_spacer, 1, 0)
        self.layout.addItem(self.h_spacer_2, 1, 4)

        self.btn_cancelar_baja.setObjectName(u"btn_azul")
        self.btn_eliminar_baja.setObjectName(u"btn_rojo")

        self.btn_cancelar_baja.clicked.connect(self.limpiar_campos)

    def agregar_datos(self):
        index = self.cmbx_producto_baja.currentIndex()
        if index:
            prod = self.cmbx_producto_baja.itemData(index)
            self.txt_id_baja.setText(str(prod.id))
            self.txt_producto_baja.setText(str(prod.nombre))
            self.txt_precio_baja.setText(str(prod.precio))
            self.txt_stock_baja.setText(str(prod.stock))
            self.txt_marca_baja.setText(str(prod.text))
            self.txt_categoria_baja.setText(str(prod.categoria))
        else:
            self.limpiar_campos()

    def limpiar_campos(self):
        for txt in self.txts:
            txt.setText("")
