from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QSpacerItem, QPushButton, QSizePolicy, QSpinBox
from PySide2.QtWidgets import QComboBox
from PySide2.QtGui import QDoubleValidator


class AltaProducto(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_producto_alta = QLabel("Producto", self)
        self.txt_producto_alta = QLineEdit(self)
        self.lbl_precio_alta = QLabel("Precio", self)
        self.txt_precio_alta = QLineEdit(self)
        self.lbl_stock_alta = QLabel("Stock", self)
        self.txt_stock_alta = QSpinBox(self)
        self.lbl_categoria_alta = QLabel("Categoria", self)
        self.cmbx_categoria_alta = QComboBox(self)
        self.lbl_marca_alta = QLabel("Marca", self)
        self.cmbx_marca_alta = QComboBox(self)
        self.btn_agregar_alta = QPushButton("Agregar", self)
        self.btn_cancelar_alta = QPushButton("Cancelar", self)

        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.txt_producto_alta.setMinimumSize(250, 0)
        self.txt_precio_alta.setValidator(QDoubleValidator())

        self.layout.addWidget(self.lbl_producto_alta, 1, 1)
        self.layout.addWidget(self.txt_producto_alta, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_precio_alta, 2, 1)
        self.layout.addWidget(self.txt_precio_alta, 2, 2, 1, 2)

        self.layout.addWidget(self.lbl_stock_alta, 3, 1)
        self.layout.addWidget(self.txt_stock_alta, 3, 2, 1, 2)

        self.layout.addWidget(self.lbl_categoria_alta, 4, 1)
        self.layout.addWidget(self.cmbx_categoria_alta, 4, 2, 1, 2)

        self.layout.addWidget(self.lbl_marca_alta, 5, 1)
        self.layout.addWidget(self.cmbx_marca_alta, 5, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_alta, 7, 2)
        self.layout.addWidget(self.btn_agregar_alta, 7, 3)

        self.layout.addItem(self.h_spacer, 1, 0)
        self.layout.addItem(self.v_spacer, 6, 3)
        self.layout.addItem(self.h_spacer_2, 1, 5)
        self.layout.addItem(self.v_spacer_2, 0, 3)
        self.layout.addItem(self.v_spacer_3, 8, 3)

        self.btn_cancelar_alta.setObjectName(u"btn_rojo")
        self.btn_agregar_alta.setObjectName(u"btn_azul")

        self.btn_cancelar_alta.clicked.connect(self.limpiar_campos)

    def limpiar_campos(self):
        self.txt_producto_alta.setText("")
        self.txt_precio_alta.setText("")
        self.txt_stock_alta.setValue(0)
        self.cmbx_marca_alta.setCurrentIndex(0)
        self.cmbx_categoria_alta.setCurrentIndex(0)
