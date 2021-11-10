from PySide2.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QAbstractItemView


class ConsultaCategoria(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.tbl_consulta = QTableWidget(self)

        self.setup_ui()

    def setup_ui(self):
        self.tbl_consulta.setColumnCount(3)
        item_id = QTableWidgetItem("ID")
        self.tbl_consulta.setHorizontalHeaderItem(0, item_id)
        item_categoria = QTableWidgetItem("Categoria")
        self.tbl_consulta.setHorizontalHeaderItem(1, item_categoria)
        item_descripcion = QTableWidgetItem("Descripcion")
        self.tbl_consulta.setHorizontalHeaderItem(2, item_descripcion)
        self.tbl_consulta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_consulta.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_consulta.setSortingEnabled(True)
        self.tbl_consulta.setCornerButtonEnabled(False)
        self.tbl_consulta.setRowCount(0)
        self.tbl_consulta.horizontalHeader().setStretchLastSection(True)

        self.layout.addWidget(self.tbl_consulta, 0, 0)
