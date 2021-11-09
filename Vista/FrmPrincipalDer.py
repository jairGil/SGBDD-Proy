from PySide2.QtWidgets import QFrame, QGridLayout, QSpacerItem, QSizePolicy, QStackedWidget


class FrmPrincipalDer(QFrame):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.stack = QStackedWidget(self)

        self.setup_ui()

    def setup_ui(self):
        self.grid_layout.addItem(QSpacerItem(20, 5, vData=QSizePolicy.Minimum), 0, 1)
        self.grid_layout.addItem(QSpacerItem(20, 5, vData=QSizePolicy.Minimum), 2, 1)
        self.grid_layout.addItem(QSpacerItem(5, 5, hData=QSizePolicy.Expanding), 1, 0)
        self.grid_layout.addItem(QSpacerItem(5, 20, hData=QSizePolicy.Expanding), 1, 2)
        self.grid_layout.addWidget(self.stack, 1, 1)

        self.stack.setStyleSheet("background-color: red;")
        self.stack.setMinimumSize(800, 600)


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    frm = FrmPrincipalDer()
    frm.show()
    sys.exit(app.exec_())
