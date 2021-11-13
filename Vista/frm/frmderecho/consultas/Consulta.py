from typing import Optional

from PySide2.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QAbstractItemView


class Consulta(QWidget):
    def __init__(self, columnas: list, datos=Optional[list]):
        super().__init__()
        if datos is None:
            datos = [None]
        self.layout = QGridLayout(self)
        self.tbl_consulta = QTableWidget(self)
        self.columnas = columnas
        self.datos = datos

        self.setup_ui()

    def setup_ui(self):
        self.layout.setMargin(0)
        self.tbl_consulta.setColumnCount(len(self.columnas))
        self.tbl_consulta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_consulta.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_consulta.setSortingEnabled(True)
        self.tbl_consulta.setCornerButtonEnabled(False)
        self.tbl_consulta.setRowCount(0)
        self.tbl_consulta.horizontalHeader().setStretchLastSection(True)

        for i, col in enumerate(self.columnas):
            item_id = QTableWidgetItem(col)
            self.tbl_consulta.setHorizontalHeaderItem(i, item_id)

        self.layout.addWidget(self.tbl_consulta, 0, 0)
