from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QSpacerItem, QSizePolicy, QComboBox, QLabel, QPushButton


class BajaModoPago(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_mpago_baja = QLabel("Modo Pago", self)
        self.cmbx_mpago_baja = QComboBox(self)
        self.lbl_detalles_baja = QLabel("Detalles", self)
        self.lbl_id_baja = QLabel("ID", self)
        self.txt_id_baja = QLineEdit(self)
        self.lbl_nombre_baja = QLabel("Nombre", self)
        self.txt_nombre_baja = QLineEdit(self)
        self.lbl_detalle_baja = QLabel("Detalles", self)
        self.txt_detalle_baja = QLineEdit(self)
        self.btn_cancelar_baja = QPushButton("Cancelar", self)
        self.btn_eliminar_baja = QPushButton("Eliminar", self)

        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.cmbx_mpago_baja.setMinimumSize(250, 0)
        self.txt_id_baja.setEnabled(False)
        self.txt_nombre_baja.setEnabled(False)
        self.txt_detalle_baja.setEnabled(False)

        self.layout.addWidget(self.lbl_mpago_baja, 1, 1)
        self.layout.addWidget(self.cmbx_mpago_baja, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_detalles_baja, 2, 1)

        self.layout.addWidget(self.lbl_id_baja, 3, 1)
        self.layout.addWidget(self.txt_id_baja, 3, 2, 1, 2)

        self.layout.addWidget(self.lbl_nombre_baja, 4, 1)
        self.layout.addWidget(self.txt_nombre_baja, 4, 2, 1, 2)

        self.layout.addWidget(self.lbl_detalle_baja, 5, 1)
        self.layout.addWidget(self.txt_detalle_baja, 5, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_baja, 7, 2)
        self.layout.addWidget(self.btn_eliminar_baja, 7, 3)

        self.layout.addItem(self.v_spacer, 6, 1)
        self.layout.addItem(self.v_spacer_2, 0, 1)
        self.layout.addItem(self.v_spacer_3, 8, 1)
        self.layout.addItem(self.h_spacer, 1, 0)
        self.layout.addItem(self.h_spacer_2, 1, 4)

        self.btn_cancelar_baja.setObjectName(u"btn_azul")
        self.btn_eliminar_baja.setObjectName(u"btn_rojo")
