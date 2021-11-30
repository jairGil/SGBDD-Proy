from PySide2.QtWidgets import *
import sys

from Modelo.ModoPago import ModoPago
from Vista.frm.FrmApp import FrmApp


class Window(QMainWindow):
    modo_pagos = []

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
            combo_box.addItem(ing(i), i)

        print(combo_box.itemData(2))


"""
    App = QApplication(sys.argv)
    
    window = Window()
    
    sys.exit(App.exec_())
"""

if __name__ == '__main__':
    import sys

    """app = QApplication(sys.argv)
    frm = FrmApp()
    sys.exit(app.exec_())"""
    ing = "dfh"
    ing2 = ""

    if ing and ing2:
        print("Dentro del if")
    else:
        print("Len = 0")

