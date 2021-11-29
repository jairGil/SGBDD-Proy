from typing import Optional

from PySide2.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QAbstractItemView


class Consulta(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.tbl_consulta = QTableWidget(self)

        self.setup_ui()

    def setup_ui(self):
        self.layout.setMargin(0)
        self.tbl_consulta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_consulta.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_consulta.setSortingEnabled(True)
        self.tbl_consulta.setCornerButtonEnabled(False)
        self.tbl_consulta.verticalHeader().hide()
        self.tbl_consulta.setRowCount(0)
        self.tbl_consulta.horizontalHeader().setStretchLastSection(True)

        self.layout.addWidget(self.tbl_consulta, 0, 0)

    def agrega_items(self, encabezados, datos):
        self.agrega_encabezados(encabezados)
        self.agrega_datos(datos)

    def agrega_encabezados(self, encabezados):
        self.tbl_consulta.setColumnCount(len(encabezados))
        self.tbl_consulta.setHorizontalHeaderLabels(encabezados)

    def agrega_datos(self, datos):
        self.tbl_consulta.setRowCount(len(datos))
        for i, dato in enumerate(datos):
            for j, campo in enumerate(dato):
                self.tbl_consulta.setItem(i, j, QTableWidgetItem(campo.__str__()))
