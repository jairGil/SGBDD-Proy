from PySide2.QtCore import QDate, QLocale
from PySide2.QtWidgets import QDateEdit, QFrame, QGridLayout, QLabel, QPushButton, QRadioButton, QWidget

from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmInicio(QFrame):
    def __init__(self, p: QWidget) -> None:
        super().__init__(parent=p)
        self.gridLayout = QGridLayout(self)
        self.rbtn_dia = QRadioButton("Dia", self)
        self.rbtn_mes = QRadioButton("Mes", self)
        self.rbtn_anio = QRadioButton("Año", self)
        self.rbtn_rango = QRadioButton("Rango", self)
        self.lbl_fecha_inicio = QLabel("Fecha de inicio", self)
        self.lbl_fecha_fin = QLabel("Fecha de Fin", self)
        self.ded_dia = QDateEdit(self)
        self.ded_mes = QDateEdit(self)
        self.ded_anio = QDateEdit(self)
        self.ded_fecha_inicio = QDateEdit(self)
        self.ded_fecha_fin = QDateEdit(self)
        self.btn_buscar = QPushButton("Buscar", self)

        self.tbl_consulta = Consulta([], [])

        self.radio_buttons = [self.rbtn_dia, self.rbtn_mes, self.rbtn_anio, self.rbtn_rango]
        self.dates = [self.ded_dia, self.ded_mes, self.ded_anio, self.ded_fecha_inicio, self.ded_fecha_fin]

        self.setup_ui()
        self.deshabilita_fechas()
        self.show()

    def setup_ui(self):
        # Añadiendo los radio buttons
        self.gridLayout.addWidget(self.rbtn_dia, 0, 0)
        self.gridLayout.addWidget(self.rbtn_mes, 0, 1)
        self.gridLayout.addWidget(self.rbtn_anio, 0, 2)
        self.gridLayout.addWidget(self.rbtn_rango, 0, 3)

        # Añadiendo los labels
        self.gridLayout.addWidget(self.lbl_fecha_inicio, 1, 3)
        self.gridLayout.addWidget(self.lbl_fecha_fin, 2, 3)

        # Añadiendo los date edits
        self.gridLayout.addWidget(self.ded_dia, 1, 0)
        self.gridLayout.addWidget(self.ded_mes, 1, 1)
        self.gridLayout.addWidget(self.ded_anio, 1, 2)
        self.gridLayout.addWidget(self.ded_fecha_inicio, 1, 4)
        self.gridLayout.addWidget(self.ded_fecha_fin, 2, 4)

        # Añadir el botón de búsqueda
        self.gridLayout.addWidget(self.btn_buscar, 0, 5, 3, 1)

        # Añadir la tabla de consultas
        self.gridLayout.addWidget(self.tbl_consulta, 3, 0, 1, 6)

        # Añadir los valores por defecto a cada date edit
        for ded in self.dates:
            ded.setDate(QDate.currentDate())
            ded.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        for rbutton in self.radio_buttons:
            rbutton.toggled.connect(self.activa_campos)

        self.retranslate_ui()

    def retranslate_ui(self):
        self.ded_dia.setDisplayFormat("dd/MMMM/yyyy")
        self.ded_mes.setDisplayFormat("MMMM/yyyy")
        self.ded_anio.setDisplayFormat("yyyy")
        self.ded_fecha_inicio.setDisplayFormat("dd/MMMM/yyyy")
        self.ded_fecha_fin.setDisplayFormat("dd/MMMM/yyyy")

    def activa_campos(self):
        if self.rbtn_dia.isChecked():
            self.deshabilita_fechas()
            self.ded_dia.setEnabled(True)
        if self.rbtn_mes.isChecked():
            self.deshabilita_fechas()
            self.ded_mes.setEnabled(True)
        if self.rbtn_anio.isChecked():
            self.deshabilita_fechas()
            self.ded_anio.setEnabled(True)
        if self.rbtn_rango.isChecked():
            self.deshabilita_fechas()
            self.ded_fecha_inicio.setEnabled(True)
            self.ded_fecha_fin.setEnabled(True)

    def deshabilita_fechas(self):
        for ded in self.dates:
            ded.setEnabled(False)
