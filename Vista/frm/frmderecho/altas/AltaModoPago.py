from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QSpacerItem, QPushButton, QSizePolicy


class AltaModoPago(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_mpago_alta = QLabel("Modo Pago", self)
        self.txt_mpago_alta = QLineEdit(self)
        self.lbl_detalles_alta = QLabel("Detalles", self)
        self.txt_detalles_alta = QLineEdit(self)
        self.btn_agregar_alta = QPushButton("Agregar", self)
        self.btn_cancelar_alta = QPushButton("Cancelar", self)

        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.txt_mpago_alta.setMinimumSize(250, 0)

        self.layout.addWidget(self.lbl_mpago_alta, 1, 1)
        self.layout.addWidget(self.txt_mpago_alta, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_detalles_alta, 2, 1)
        self.layout.addWidget(self.txt_detalles_alta, 2, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_alta, 4, 2)
        self.layout.addWidget(self.btn_agregar_alta, 4, 3)

        self.layout.addItem(self.h_spacer, 1, 0)
        self.layout.addItem(self.h_spacer_2, 1, 4)
        self.layout.addItem(self.v_spacer_2, 0, 2)
        self.layout.addItem(self.v_spacer, 3, 2)
        self.layout.addItem(self.v_spacer_3, 5, 2)

        self.btn_cancelar_alta.setObjectName(u"btn_rojo")
        self.btn_agregar_alta.setObjectName(u"btn_azul")
