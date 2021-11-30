from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QSpacerItem, QSizePolicy, QComboBox, QLabel, QPushButton


class CambioCliente(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_cliente_cambio = QLabel("Cliente", self)
        self.cmbx_cliente_cambio = QComboBox(self)
        self.lbl_detalles_cambio = QLabel("Detalles", self)
        self.lbl_id_cambio = QLabel("ID", self)
        self.txt_id_cambio = QLineEdit(self)
        self.lbl_nombre_cambio = QLabel("Nombre", self)
        self.txt_nombre_cambio = QLineEdit(self)
        self.lbl_apellido_cambio = QLabel("Apellido", self)
        self.txt_apellido_cambio = QLineEdit(self)
        self.lbl_email_cambio = QLabel("Email", self)
        self.txt_email_cambio = QLineEdit(self)
        self.lbl_telefono_cambio = QLabel("Telefono", self)
        self.txt_telefono_cambio = QLineEdit(self)
        self.btn_cancelar_cambio = QPushButton("Cancelar", self)
        self.btn_modificar_cambio = QPushButton("Modificar", self)

        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.cmbx_cliente_cambio.setMinimumSize(250, 0)
        self.txt_id_cambio.setEnabled(False)

        self.layout.addWidget(self.lbl_cliente_cambio, 1, 1)
        self.layout.addWidget(self.cmbx_cliente_cambio, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_detalles_cambio, 2, 1)

        self.layout.addWidget(self.lbl_id_cambio, 3, 1)
        self.layout.addWidget(self.txt_id_cambio, 3, 2, 1, 2)

        self.layout.addWidget(self.lbl_nombre_cambio, 4, 1)
        self.layout.addWidget(self.txt_nombre_cambio, 4, 2, 1, 2)

        self.layout.addWidget(self.lbl_apellido_cambio, 5, 1)
        self.layout.addWidget(self.txt_apellido_cambio, 5, 2, 1, 2)

        self.layout.addWidget(self.lbl_email_cambio, 6, 1)
        self.layout.addWidget(self.txt_email_cambio, 6, 2, 1, 2)

        self.layout.addWidget(self.lbl_telefono_cambio, 7, 1)
        self.layout.addWidget(self.txt_telefono_cambio, 7, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_cambio, 9, 2)
        self.layout.addWidget(self.btn_modificar_cambio, 9, 3)

        self.layout.addItem(self.v_spacer, 0, 1)
        self.layout.addItem(self.v_spacer_2, 8, 1)
        self.layout.addItem(self.v_spacer_3, 10, 1)
        self.layout.addItem(self.h_spacer, 1, 0)
        self.layout.addItem(self.h_spacer_2, 1, 4)

        self.btn_cancelar_cambio.setObjectName(u"btn_rojo")
        self.btn_modificar_cambio.setObjectName(u"btn_azul")

        self.btn_cancelar_cambio.clicked.connect(self.limpiar_campos)

    def agregar_datos(self):
        index = self.cmbx_cliente_cambio.currentIndex()
        if index:
            cliente = self.cmbx_cliente_cambio.itemData(index)
            self.txt_id_cambio.setText(str(cliente.id))
            self.txt_nombre_cambio.setText(str(cliente.nombre))
            self.txt_apellido_cambio.setText(str(cliente.apellido))
            self.txt_email_cambio.setText(str(cliente.email))
            self.txt_telefono_cambio.setText(str(cliente.telefono))
        else:
            self.limpiar_campos()

    def limpiar_campos(self):
        self.txt_id_cambio.setText("")
        self.txt_nombre_cambio.setText("")
        self.txt_apellido_cambio.setText("")
        self.txt_email_cambio.setText("")
        self.txt_telefono_cambio.setText("")
