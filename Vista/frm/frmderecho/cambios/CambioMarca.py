from PySide2.QtWidgets import QWidget, QGridLayout, QSpacerItem, QLabel, QSizePolicy, QComboBox, QLineEdit, QPushButton


class CambioMarca(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_marca_cambio = QLabel("Marca", self)
        self.cmbx_marca_cambio = QComboBox(self)
        self.lbl_detalles_cambio = QLabel("Detalles", self)
        self.lbl_id_cambio = QLabel("ID", self)
        self.txt_id_cambio = QLineEdit(self)
        self.lbl_nombre_cambio = QLabel("Nombre", self)
        self.txt_nombre_cambio = QLineEdit(self)
        self.btn_cancelar_cambio = QPushButton("Cancelar", self)
        self.btn_modificar_cambio = QPushButton("Modificar", self)

        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.cmbx_marca_cambio.setMinimumSize(250, 0)
        self.txt_id_cambio.setEnabled(False)

        self.layout.addWidget(self.lbl_marca_cambio, 1, 1)
        self.layout.addWidget(self.cmbx_marca_cambio, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_detalles_cambio, 2, 1)

        self.layout.addWidget(self.lbl_id_cambio, 3, 1)
        self.layout.addWidget(self.txt_id_cambio, 3, 2, 1, 2)

        self.layout.addWidget(self.lbl_nombre_cambio, 4, 1)
        self.layout.addWidget(self.txt_nombre_cambio, 4, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_cambio, 6, 2)
        self.layout.addWidget(self.btn_modificar_cambio, 6, 3)

        self.layout.addItem(self.v_spacer, 0, 1)
        self.layout.addItem(self.v_spacer_2, 5, 2)
        self.layout.addItem(self.v_spacer_3, 7, 2)
        self.layout.addItem(self.h_spacer, 3, 0)
        self.layout.addItem(self.h_spacer_2, 3, 4)

        self.btn_cancelar_cambio.setObjectName(u"btn_rojo")
        self.btn_modificar_cambio.setObjectName(u"btn_azul")

        self.btn_cancelar_cambio.clicked.connect(self.limpiar_campos)

    def agregar_datos(self):
        index = self.cmbx_marca_cambio.currentIndex()
        if index:
            marca = self.cmbx_marca_cambio.itemData(index)
            self.txt_id_cambio.setText(str(marca.id))
            self.txt_nombre_cambio.setText(str(marca.nombre))
        else:
            self.limpiar_campos()

    def limpiar_campos(self):
        self.cmbx_marca_cambio.setCurrentIndex(0)
        self.txt_id_cambio.setText("")
        self.txt_nombre_cambio.setText("")
