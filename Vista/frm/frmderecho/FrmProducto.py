from PySide2.QtWidgets import QTabWidget, QWidget

from Controlador.DMLCategoria import DMLCategoria
from Controlador.DMLMarca import DMLMarca
from Controlador.DMLProducto import DMLProducto
from Modelo.Categoria import Categoria
from Modelo.Marca import Marca
from Modelo.Producto import Producto
from Vista.dlg.DlgAviso import DlgAviso
from Vista.frm.frmderecho.altas.AltaProducto import AltaProducto
from Vista.frm.frmderecho.bajas.BajaProducto import BajaProducto
from Vista.frm.frmderecho.cambios.CambioProducto import CambioProducto
from Vista.frm.frmderecho.consultas.Consulta import Consulta


class FrmProducto(QTabWidget):
    __dlg_aviso: DlgAviso

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.conexion = self.parent().conexion
        self.dml = DMLProducto(self.conexion)

        self.alta = AltaProducto()
        self.baja = BajaProducto()
        self.cambio = CambioProducto()
        self.consulta = Consulta()

        self.setup_ui()
        self.agrega_items()
        self.agrega_acciones_cmbx()
        self.agrega_acciones_btn()

    def setup_ui(self):
        self.addTab(self.alta, "Alta")
        self.addTab(self.baja, "Baja")
        self.addTab(self.cambio, "Cambio")
        self.addTab(self.consulta, "Consulta")

    def agrega_items(self):
        encabezados, datos_tabla = self.dml.consulta_tabla()
        datos_prod = self.dml.consulta()

        self.alta.cmbx_categoria_alta.addItem("")
        self.alta.cmbx_marca_alta.addItem("")
        self.baja.cmbx_producto_baja.addItem("")
        self.cambio.cmbx_producto_cambio.addItem("")
        self.cambio.cmbx_marca_cambio.addItem("")
        self.cambio.cmbx_categoria_cambio.addItem("")
        self.alta.cmbx_categoria_alta.setItemText(0, "Seleccione una opcion")
        self.alta.cmbx_marca_alta.setItemText(0, "Seleccione una opcion")
        self.baja.cmbx_producto_baja.setItemText(0, "Seleccione una opcion")
        self.cambio.cmbx_producto_cambio.setItemText(0, "Seleccione una opcion")
        self.cambio.cmbx_marca_cambio.setItemText(0, "Seleccione una opcion")
        self.cambio.cmbx_categoria_cambio.setItemText(0, "Seleccione una opcion")

        if datos_prod and encabezados:
            self.consulta.agrega_items(encabezados, datos_tabla)
            for reg in datos_prod:
                producto = Producto(id=reg[0], nombre=reg[1], precio=reg[2], stock=reg[3],
                                    marca=reg[4], categoria=reg[5])
                self.baja.cmbx_producto_baja.addItem(str(producto), producto)
                self.cambio.cmbx_producto_cambio.addItem(str(producto), producto)

        dml_aux = DMLCategoria(self.conexion)
        datos_aux = dml_aux.consulta()
        for reg in datos_aux:
            cat = Categoria(reg[0], reg[1], reg[2])
            self.alta.cmbx_categoria_alta.addItem(str(cat), cat)
            self.cambio.cmbx_categoria_cambio.addItem(str(cat), cat)

        dml_aux = DMLMarca(self.conexion)
        _, datos_aux = dml_aux.consulta()
        for reg in datos_aux:
            mar = Marca(reg[0], reg[1])
            self.alta.cmbx_marca_alta.addItem(str(mar), mar)
            self.cambio.cmbx_marca_cambio.addItem(str(mar), mar)

    def agrega_acciones_cmbx(self):
        self.baja.cmbx_producto_baja.currentIndexChanged.connect(self.baja.agregar_datos)
        self.cambio.cmbx_producto_cambio.currentIndexChanged.connect(self.cambio.agregar_datos)

    def agrega_acciones_btn(self):
        self.alta.btn_agregar_alta.clicked.connect(self.insertar_db)
        self.baja.btn_eliminar_baja.clicked.connect(self.eliminar_db)
        self.cambio.btn_modificar_cambio.clicked.connect(self.modificar_db)

    def insertar_db(self):
        index_marca = self.alta.cmbx_marca_alta.currentIndex()
        index_categoria = self.alta.cmbx_categoria_alta.currentIndex()
        nombre = self.alta.txt_producto_alta.text()
        precio = float(self.alta.txt_precio_alta.text())
        stock = int(self.alta.txt_stock_alta.text())

        if nombre and precio and stock:
            if index_categoria and index_marca:
                marca = int(self.alta.cmbx_marca_alta.itemData(index_marca).id)
                categoria = int(self.alta.cmbx_categoria_alta.itemData(index_categoria).id)
                print(marca, " ", categoria)
                id = self.dml.obten_id()
                producto = Producto(id=id, nombre=nombre, precio=precio, stock=stock, marca=marca, categoria=categoria)
                self.dml.alta(producto)
                self.alta.limpiar_campos()
                self.baja.cmbx_producto_baja.addItem(str(producto), producto)
                self.cambio.cmbx_producto_cambio.addItem(str(producto), producto)
                self.__dlg_aviso = DlgAviso(self, "Registro agregado correctamente.")
                self.actualiza_tabla()
            else:
                if not (index_categoria or index_marca):
                    self.__dlg_aviso = DlgAviso(self, "ERROR: Selecciona una marca y una categoria")
                if not index_categoria:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: Selecciona una categoria")
                if not index_marca:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: Selecciona una marca")

        else:
            if not (nombre or precio or stock):
                self.__dlg_aviso = DlgAviso(self, "ERROR: Los campos solicitados se encuentran vacíos")
            elif not nombre:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo nombre está vacío")
            elif not precio:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo precio está vacío")
            elif not stock:
                self.__dlg_aviso = DlgAviso(self, "ERROR: El campo stock está vacío")

    def eliminar_db(self):
        index = self.baja.cmbx_cliente_baja.currentIndex()
        if index:
            id = int(self.baja.txt_id_baja.text())
            self.dml.baja(id)
            self.baja.cmbx_cliente_baja.removeItem(index)
            self.cambio.cmbx_cliente_cambio.removeItem(index)
            self.__dlg_aviso = DlgAviso(self, "Registro eliminado con exito.")
            self.actualiza_tabla()
        else:
            self.__dlg_aviso = DlgAviso(self, "Primero debe seleccionar un elemento del combo box")

    def modificar_db(self):
        index = self.cambio.cmbx_producto_cambio.currentIndex()
        idx_categoria = self.cambio.cmbx_categoria_cambio.currentIndex()
        idx_marca = self.cambio.cmbx_marca_cambio.currentIndex()
        nombre = self.cambio.txt_nombre_cambio.text()
        stock = int(self.cambio.txt_stock_cambio.text())
        precio = float(self.cambio.txt_precio_cambio.text())

        if index and idx_marca and idx_categoria:
            if nombre and stock and precio:
                prod = self.cambio.cmbx_producto_cambio.itemData(index)
                prod.nombre = nombre
                prod.stock = stock
                prod.precio = precio
                prod.marca = int(self.cambio.cmbx_marca_cambio.itemData(idx_marca).id)
                prod.categoria = int(self.cambio.cmbx_categoria_cambio.itemData(idx_categoria).id)

                self.dml.cambio(prod)

                self.cambio.cmbx_producto_cambio.setItemText(index, str(prod))
                self.cambio.cmbx_producto_cambio.setItemData(index, prod)

                self.baja.cmbx_producto_baja.setItemText(index, str(prod))
                self.baja.cmbx_producto_baja.setItemData(index, prod)

                self.cambio.limpiar_campos()
                self.__dlg_aviso = DlgAviso(self, "Registro modificado correctamente")
                self.actualiza_tabla()
            else:
                if not (nombre or stock or precio):
                    self.__dlg_aviso = DlgAviso(self, "ERROR: Los campos solicitados están vacíos")
                elif not nombre:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo nombre está vacío")
                elif not precio:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo precio está vacío")
                elif not stock:
                    self.__dlg_aviso = DlgAviso(self, "ERROR: El campo stock está vacío")
        else:
            if not (index or idx_marca or idx_categoria):
                self.__dlg_aviso = DlgAviso(self, "ERROR: Seleccione un registro de los combo boxes")
            elif not index:
                self.__dlg_aviso = DlgAviso(self, "ERROR: Seleccione un producto de los combo boxes")
            elif not idx_marca:
                self.__dlg_aviso = DlgAviso(self, "ERROR: Seleccione una marca de los combo boxes")
            elif not idx_categoria:
                self.__dlg_aviso = DlgAviso(self, "ERROR: Seleccione una categoria de los combo boxes")

    def actualiza_tabla(self):
        encabezados, datos = self.dml.consulta_tabla()
        self.consulta.agrega_items(encabezados, datos)


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = FrmProducto()
    w.show()
    sys.exit(app.exec_())
