from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QSpacerItem, QSizePolicy, QComboBox, QLabel, QPushButton


class BajaCliente(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_cliente_baja = QLabel("Cliente", self)
        self.cmbx_cliente_baja = QComboBox(self)
        self.lbl_detalles_baja = QLabel("Detalles", self)
        self.lbl_id_baja = QLabel("ID", self)
        self.txt_id_baja = QLineEdit(self)
        self.lbl_nombre_baja = QLabel("Nombre", self)
        self.txt_nombre_baja = QLineEdit(self)
        self.lbl_apellido_baja = QLabel("Apellido", self)
        self.txt_apellido_baja = QLineEdit(self)
        self.lbl_email_baja = QLabel("Email", self)
        self.txt_email_baja = QLineEdit(self)
        self.lbl_telefono_baja = QLabel("Telefono", self)
        self.txt_telefono_baja = QLineEdit(self)
        self.btn_cancelar_baja = QPushButton("Cancelar", self)
        self.btn_eliminar_baja = QPushButton("Eliminar", self)

        self.txts = [self.txt_id_baja, self.txt_nombre_baja, self.txt_apellido_baja, self.txt_email_baja,
                     self.txt_telefono_baja]

        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.cmbx_cliente_baja.setMinimumSize(250, 0)

        for txt in self.txts:
            txt.setEnabled(False)

        self.layout.addWidget(self.lbl_cliente_baja, 1, 1)
        self.layout.addWidget(self.cmbx_cliente_baja, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_detalles_baja, 2, 1)

        self.layout.addWidget(self.lbl_id_baja, 3, 1)
        self.layout.addWidget(self.txt_id_baja, 3, 2, 1, 2)

        self.layout.addWidget(self.lbl_nombre_baja, 4, 1)
        self.layout.addWidget(self.txt_nombre_baja, 4, 2, 1, 2)

        self.layout.addWidget(self.lbl_apellido_baja, 5, 1)
        self.layout.addWidget(self.txt_apellido_baja, 5, 2, 1, 2)

        self.layout.addWidget(self.lbl_email_baja, 6, 1)
        self.layout.addWidget(self.txt_email_baja, 6, 2, 1, 2)

        self.layout.addWidget(self.lbl_telefono_baja, 7, 1)
        self.layout.addWidget(self.txt_telefono_baja, 7, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_baja, 9, 2)
        self.layout.addWidget(self.btn_eliminar_baja, 9, 3)

        self.layout.addItem(self.v_spacer, 0, 0)
        self.layout.addItem(self.v_spacer_2, 8, 1)
        self.layout.addItem(self.v_spacer_3, 10, 1)
        self.layout.addItem(self.h_spacer, 1, 0)
        self.layout.addItem(self.h_spacer_2, 1, 4)

        self.btn_cancelar_baja.setObjectName(u"btn_azul")
        self.btn_eliminar_baja.setObjectName(u"btn_rojo")
