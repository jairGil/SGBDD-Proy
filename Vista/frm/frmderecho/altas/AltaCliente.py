from PySide2.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QSpacerItem, QPushButton, QSizePolicy
from PySide2.QtGui import QDoubleValidator


class AltaCliente(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.lbl_email_alta = QLabel("Email", self)
        self.txt_email_alta = QLineEdit(self)
        self.lbl_nombre_alta = QLabel("Nombre", self)
        self.txt_nombre_alta = QLineEdit(self)
        self.lbl_apellido_alta = QLabel("Apellido", self)
        self.txt_apellido_alta = QLineEdit(self)
        self.lbl_telefono_alta = QLabel("Telefono", self)
        self.txt_telefono_alta = QLineEdit(self)
        self.btn_agregar_alta = QPushButton("Agregar", self)
        self.btn_cancelar_alta = QPushButton("Cancelar", self)

        self.h_spacer = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.h_spacer_2 = QSpacerItem(40, 20, hData=QSizePolicy.Expanding)
        self.v_spacer = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_2 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)
        self.v_spacer_3 = QSpacerItem(20, 40, vData=QSizePolicy.Expanding)

        self.setup_ui()

    def setup_ui(self):
        self.txt_email_alta.setMinimumSize(250, 0)
        self.txt_nombre_alta.setValidator(QDoubleValidator())

        self.layout.addWidget(self.lbl_email_alta, 1, 1)
        self.layout.addWidget(self.txt_email_alta, 1, 2, 1, 2)

        self.layout.addWidget(self.lbl_nombre_alta, 2, 1)
        self.layout.addWidget(self.txt_nombre_alta, 2, 2, 1, 2)

        self.layout.addWidget(self.lbl_apellido_alta, 3, 1)
        self.layout.addWidget(self.txt_apellido_alta, 3, 2, 1, 2)

        self.layout.addWidget(self.lbl_telefono_alta, 4, 1)
        self.layout.addWidget(self.txt_telefono_alta, 4, 2, 1, 2)

        self.layout.addWidget(self.btn_cancelar_alta, 6, 2)
        self.layout.addWidget(self.btn_agregar_alta, 6, 3)

        self.layout.addItem(self.h_spacer, 1, 0)
        self.layout.addItem(self.v_spacer, 5, 3)
        self.layout.addItem(self.h_spacer_2, 1, 5)
        self.layout.addItem(self.v_spacer_2, 0, 3)
        self.layout.addItem(self.v_spacer_3, 7, 3)

        self.btn_cancelar_alta.setObjectName(u"btn_rojo")
        self.btn_agregar_alta.setObjectName(u"btn_azul")
