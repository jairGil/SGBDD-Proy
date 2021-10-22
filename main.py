from PySide2.QtWidgets import *
import sys

from Modelo.ModoPago import ModoPago


class Window(QMainWindow):
    modo_pagos = []
    list1 = []

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100, 600, 400)

        modo_pago = ModoPago(1, "efectivo", "pagos en efectivo")
        self.modo_pagos.append(modo_pago)
        modo_pago = ModoPago(2, "tarjeta", "pagos con tarjeta")
        self.modo_pagos.append(modo_pago)
        modo_pago = ModoPago(3, "linea", "pagos en linea")
        self.modo_pagos.append(modo_pago)

        for i in self.modo_pagos:
            print(i)
        print(self.modo_pagos)

        self.ui_components()

        self.show()

    def ui_components(self):
        combo_box = QComboBox(self)
        combo_box.setGeometry(200, 150, 120, 40)

        for i in self.modo_pagos:
            combo_box.addItem(i.__str__(), i)

        print(combo_box.itemData(2).detalles)


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec_())
